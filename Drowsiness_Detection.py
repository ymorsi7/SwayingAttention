from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib #import for facial detection files
import cv2
from ECE16Lib.Communication import Communication
import time
import numpy as np
import matplotlib.pyplot as plt
def eye_aspect_ratio(eye):
    #equation for finding the eye aspect ratio. 
    #this equation takes 6 points that are used for eye detection
    #and compares them to create a ratio for detecting how open your 
    #eyes are. We can use this as a factor of determinion how awake or how much someone
    #is paying attention. 
	A = distance.euclidean(eye[1], eye[5]) #vertical distance (top and bottom of eye)
	B = distance.euclidean(eye[2], eye[4]) #vertical distance (top and bottom of eye)
	C = distance.euclidean(eye[0], eye[3]) #Horizonatal distance (top and bottom of eye)
	ratio = (A + B) / (2.0 * C) #ratio of vertical to horizontal
	return ratio
comms = Communication("COM4", 115200) #connecting to Arduino
comms.clear()                   # just in case any junk is in the pipes
comms.send_message("live")  # begin sending data
thresh = 0.265 #eye-aspect-ratio threshold value for Drowsiness detection 
plt.style.use('seaborn-whitegrid') #graph for data collection
ppg = np.array([])  #eye-ratio data collection array
t_array = np.array([]) #time collection array for data
frame_check = 20 #Amount of conescutive frames needed for detected Drowsiness  
detect = dlib.get_frontal_face_detector() #using c++ files from dlib for facial detection
predict = dlib.shape_predictor(".\shape_predictor_68_face_landmarks.dat")# dlib c++ file that detects facial parts like eyes, nose, lip etc.

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"] #initilizing variables for left eye detection. 
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"] #initilizing variables for right eye detections.
cap=cv2.VideoCapture(0) #start camera
lim=0 # initilizing number of frames of Drowsiness in a row variable
while True:
	ret, frame=cap.read() #start reading from camera
	frame = imutils.resize(frame, width=450) #setting frame input size
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #gray scaling input frames
	subjects = detect(gray, 0) # subjects stores data from perfroming frontal face detection on grayscaled input frames. 
	for subject in subjects:
		shape = predict(gray, subject) #Identifies facial features on gray scaled input using facial detection
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd] #Numpy Array for left eye.
		rightEye = shape[rStart:rEnd] #Numpy Array for right eye.
		leftEAR = eye_aspect_ratio(leftEye) #Eye aspect ratio of left eye
		rightEAR = eye_aspect_ratio(rightEye) #Eye aspect ratio of right eye
		ratio = (leftEAR + rightEAR) / 2.0 #Average of left and right eye ratio
		leftEyeHull = cv2.convexHull(leftEye) #image for eye traceing on input frame
		rightEyeHull = cv2.convexHull(rightEye)#image for eye traceing on input frame
		ppg = np.append(ppg,ratio)# data collection for the average of left and right eye ratio. 
		t_array = np.append(t_array,time.time())#collecting time for data
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)#draw hull over left eye in cv2 imshow frame
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)#draw hull over right eye in cv2 imshow frame
		if ratio < thresh: # detects if the ratio goes below the threshold (Drowsiness detected)
			lim += 1 #adds one to frames of Drowsiness detected in a row
			print (lim) #printing value for testing/debugging
			if lim >= frame_check: #Checks if the number of consecutive Drowsiness detection frames is above set amount. This means overall 
                                    #Drowsiness is detected and a warning should be sent out.
                
			    cv2.putText(frame, "Drowsiness Detected!", (10, 30),  #outputs Drowsiness detected on imshow frame
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2) #setting font/size/color/location
			    comms.send_message("Wake up!")#sending alert message to Arduino to display on OLED
			    comms.send_message("on!")#sending command to turn on buzzer 
		else:                             #if overall Drowsiness is not detected
			comms.send_message("off") #command to turn of buzzer
			lim = 0                   #set consequtive frames of Drowsiness detection to 0
	#cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
	#resize = cv2.resize(cap,(960,540))
	cv2.imshow("Frame",frame)          #showes frame input with eye traceing overlay/ displayed Drowsiness detection when required
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):                #Code for exiting program
		break
p = ppg[3:] #remove first few points because of auto-exposure    
filename = "Yusuf_sunglass5.csv" #filename for storing data

fig = plt.figure() #setting up plot
ax = plt.axes() #plot setup    
x = np.linspace(0, 1, len(p))

p = ppg[60:] #taking out more data points at the start for collecting data.  

t = t_array[60:]-t_array[10] #time for data

ax.set_xlabel("time(s)") #plot setup
ax.set_ylabel("Eye-Aspect-ratio") #plot setup
datt = np.vstack((t*1000,p)).T #Data being stored

#np.savetxt(filename, datt ,delimiter=",") # line for saving data file

ax.plot(t, p)    #plotting
comms.send_message("off")
comms.send_message("sleep")  # stop sending data
comms.close()
cv2.destroyAllWindows()
#cap.stop()
