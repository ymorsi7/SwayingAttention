const int accelX = A0;

void setup() {
  // Begin the Serial communication (you did this in the last lab!)
  Serial.begin(9600);
  // Define the analog pin as input
  pinMode(accelX, INPUT);

}

void loop() {
  int accel_val = analogRead(accelX);
  Serial.println(accel_val);

}
