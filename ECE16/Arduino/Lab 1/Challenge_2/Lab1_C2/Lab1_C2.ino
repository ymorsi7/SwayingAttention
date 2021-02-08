const int pushButton = 14;
unsigned long timeVar = 0;
unsigned long timeVar2 = 0;
unsigned long timeVarCounter = 0;
int buttonState = 0;
int count = 0;

void setup() {
  Serial.begin(9600); // startup serial monitor
  pinMode(pushButton, INPUT); // telling the computer that the button is an input device
}

void loop() {
  buttonState = digitalRead(pushButton); // reading on button is button state
  timeVar = millis(); 
 
if (buttonState == HIGH) {
  if (count == 1){
    count = 0;
  }
  else{
    count = 1;
    }
  }
  
 if(count == 1){
  timeVar2 = timeVar2 + millis() - timeVar;
  timeVarCounter = timeVar2 / 1000; // conversion between ms and seconds
 }
 if(millis() % 100 == 0){
    Serial.println(timeVarCounter);
  }
}
