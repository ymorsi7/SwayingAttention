const int RED_LED = 23;
const int BLUE_LED = 22;
const int YELLOW_LED = 14;

void setup()
{
     //initialize digital pin LED_BUILTIN as an output
     pinMode(RED_LED, OUTPUT);
     pinMode(BLUE_LED, OUTPUT);
     pinMode(YELLOW_LED, OUTPUT);
     
}

void loop()
{
part1A();
//part1B();
//part1C();
//part2A();
//part2B();
//part2C();
}

void part1A(){
  digitalWrite(RED_LED, HIGH);
  delay(1000);
  digitalWrite(RED_LED, LOW);
  delay(1000);
}

void part1B(){
  digitalWrite(BLUE_LED, HIGH);
  delay(100);
  digitalWrite(BLUE_LED, LOW);
  delay(100);
}

 void part1C(){
  digitalWrite(YELLOW_LED, HIGH);
  delay(20);
  digitalWrite(YELLOW_LED, LOW);
  delay(20);
 }
 
void part2A(){
  digitalWrite(RED_LED, HIGH);
  delay(1000);
  digitalWrite(RED_LED, LOW);
  delay(100);
}

void part2B(){
  digitalWrite(BLUE_LED, HIGH);
  delay(200);
  digitalWrite(BLUE_LED, LOW);
  delay(50);
}

void part2C(){
  digitalWrite(YELLOW_LED, HIGH);
  delay(20);
  digitalWrite(YELLOW_LED, LOW);
  delay(10);
}
