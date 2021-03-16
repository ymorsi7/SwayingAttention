from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
from ECE16Lib.Communication import Communication
import time
import numpy as np
import matplotlib.pyplot as plt
def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ratio = (A + B) / (2.0 * C)
	return ratio
comms = Communication("COM4", 115200)
comms.clear()                   # just in case any junk is in the pipes
comms.send_message("wearable")  # begin sending data
thresh = 0.25 #D
plt.style.use('seaborn-whitegrid')
ppg = np.array([])
t_array = np.array([])
frame_check = 20 #Amount of frames of conescutive frames needed for detected drowsiness  
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor(".\shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag=0
while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ratio = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		ppg = np.append(ppg,ratio)
		t_array = np.append(t_array,time.time())
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
		if ratio < thresh:
			flag += 1
			print (flag)
			if flag >= frame_check:
                
			    cv2.putText(frame, "Drowsiness Detected!", (10, 30),  
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			    comms.send_message("Wake up!")
			    comms.send_message("on!")
		else:
			comms.send_message("off")
			flag = 0
	#cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
	#resize = cv2.resize(cap,(960,540))
	cv2.imshow("Frame",frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
p = ppg[3:] #remove first few points because of auto-exposure    
filename = "Ratio_10_.csv"

fig = plt.figure()
ax = plt.axes()
x = np.linspace(0, 1, len(p))
#ax.plot(x, p)
p = ppg[60:]

t = t_array[60:]-t_array[10]

ax.set_xlabel("time(s)")
ax.set_ylabel("Red Channel Value")
datt = np.vstack((t*1000,p)).T

np.savetxt(filename, datt ,delimiter=",")
ax.plot(t, p)    
comms.send_message("sleep")  # stop sending data
comms.close()
cv2.destroyAllWindows()
cap.stop()
