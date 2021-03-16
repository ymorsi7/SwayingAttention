int sampleTime = 0; // Time of last sample (in Sampling tab)
// Acceleration values recorded from the readAccelSensor() function

bool sending;
 

void setup() {
  setupCommunication();
  setupDisplay();
  setupMotor();
  sending = false;
  writeDisplay("Sleep", 0, true);
}

void loop() {
  String command = receiveMessage();
  if(command == "sleep") {
    sending = false;
    writeDisplay("Sleep", 0, true);
  }
  else if(command == "wearable") {
    sending = true;
    writeDisplay("Wearable", 0, true);
  }
  else if(command == "off"){
    deactivateMotor();
  }
  else if(command == "on!"){
    activateMotor(500);
    
  }
  else if(command != " "){ 
    
    writeDisplay(command.c_str(), 0, true);
  }
 
}
