
void setup()
{
    Serial.begin(9600); 
    Serial.print("Hello world\n");
    Serial.println("Welcome to ECE 16");
}

void loop()
{
  if (Serial.available() > 0) {
  char incoming_data = Serial.read();
  Serial.print(incoming_data);
  }
}
