const int BUTTON_PIN = 14; // map BUTTON_PIN to the GPIO pin we're using
const int LED_PIN = 13; // map LED_PIN to the GPIO pin to drive the LED

void setup()
{
     //initialize button_pin as an input
     pinMode(BUTTON_PIN, INPUT);
     // pinMode(BUTTON_PIN, INPUT_PULLUP);
     //initialize digital pin LED_BUILTIN as an output
     pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{

  /*
   digitalWrite(LED_BUILTIN, HIGH); // turn the LED on
     delay(500); //wait for half a second
     digitalWrite(LED_BUILTIN, LOW); // turn the LED off
     delay(1000); //wait for a second
   */
     // if the button is pushed down, turn on the LED
     if (digitalRead(BUTTON_PIN) == LOW) {
          digitalWrite(LED_BUILTIN, HIGH);     
     }
     // if the button isn't pushed down, turn the LED off
     else {
          digitalWrite(LED_BUILTIN, LOW); // turn the LED off
     }
}
