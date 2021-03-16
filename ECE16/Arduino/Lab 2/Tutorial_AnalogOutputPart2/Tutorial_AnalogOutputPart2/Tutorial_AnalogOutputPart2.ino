void setup () {
     setupMotor();
}

void loop() {
     deactivateMotor();
     delay(2000);
     activateMotor(127);
     delay(2000);
     activateMotor(255);
     delay(2000);
     activateMotor(90);
     delay(2000);
}
