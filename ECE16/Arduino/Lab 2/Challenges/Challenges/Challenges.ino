int sampleTime = 0;
int ax = 0; 
int ay = 0;
int az = 0;
int timeVar;
const int SHORT_PRESS_TIME = 2000;
int lastState = LOW;  // the previous state from the input pin
int currentState;     // the current reading from the input pin
unsigned long pressedTime  = 0;
unsigned long releasedTime = 0;


int numTaps = 0;
const int button = 14;

void setup () {
     setupAccelSensor();
     setupDisplay();
     setupMotor();
     Serial.begin(9600);
     pinMode(button, INPUT);
}

void loop() {
  timeVar = millis(); 
     if(sampleSensors() && Serial.availableForWrite()) {
         Serial.print(ax);
         Serial.print(",");
         Serial.print(ay);
         Serial.print(",");
         Serial.println(az);  // when accelerometer is tapped, az goes over 2600
     }
    
    detectTaps(); 
    displaySampleRate();

    if(numTaps > 0){ //prevents numTaps from being negative
        numTaps = 0;
      }
      
    if(digitalRead(button) == HIGH){ // RESET WHEN BUTTON PUSHED DOWN FOR OVER 2 SECONDS
      delay(2000);
      resetNumTaps();
    }

    if((az < 2650) && (az > 2450)){ // If during the countdown, a tap 
                                    //is detected, stop the countdown process and 
                                    // increment the numTaps variable by 1.
        delay(1000);
        numTaps -= 1;
      }
    
  
      if(numTaps == 0){ // if numtaps is zero, have motor buzz
        activateMotor(255);
        delay(2000);
      }
      else{
        deactivateMotor();
        delay(2000);
      }
}


void resetNumTaps(){
  numTaps = 0;
}

void countdown(){
    numTaps = numTaps - 1;
    delay(1000);
}

int detectTaps(){
  if (az > 2650 || az < 2450){
    numTaps = numTaps + 1;
  }
}

void displaySampleRate() {
     String xString = String(numTaps);  writeDisplay(xString.c_str(), 0, true);
} 
