const int pushButton = 14;
unsigned long timeVar = 0;
unsigned long timeVar2 = 0;
unsigned long timeVarCounter = 0;
unsigned long theCounter = 0;

void setup() {
  Serial.begin(9600); // startup serial monitor
  pinMode(pushButton, INPUT);
}

void loop() {
 timeVar = millis(); 
 
  if (digitalRead(pushButton) == HIGH) {
    delay(300);
    theCounter += 1;
    timeVarCounter = 0;
    timeVar2 = 0;
    } 
 
  timeVar2 = timeVar2 + millis() - timeVar;
  timeVarCounter = timeVar2 / 1000; // conversion between ms and seconds

  if(theCounter < 0){ // to ensure there are no neg values
    theCounter = 0;
    }

  if((timeVarCounter > 3) && theCounter > 0){
      delay(200);
      theCounter = theCounter;
      theCounter -= 1;
      }
      
 if(millis() % 100 == 0){
    Serial.println(theCounter);
 }
}
