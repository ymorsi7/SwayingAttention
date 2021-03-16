# ECE16 Lab 1 Report
Prepared by: Yusuf Morsi

Date: 01/25/2021

**Tutorial_digital_communication** is a tutorial in which we experiment with not only using the built-in LED on the Sparkfun ESP32, but also with a button and a connectable LED. We utilize pinMode in void setup()
to initialize the built-in LED and button as inputs, and we use digitalWrite() and digitalRead() inside an if-statement in void loop() to set conditions for the LED to turn on and off. We also use digitalWrite() once again to set up a connectable LED, and perform the same function. 


**Tutorial_serial_communication** familiarizes us with Arduino IDE's serial monitor. We set the baud rate to 9600 using Serial.begin() in void setup(). When then include two basic messages with the Serial.print() function to run a basic Hello World program. Subsequently, we write an if-statement in void loop() (with Serial.available() > 0 as a condition) and include the char datatype to store the input from a Serial.read() function. After running this, we are able to type inputs in the serial monitor and see what we write print.

**Challenge 1** teaches us two different ideas. We not only blink three LEDs at different levels of Hz, but also turn those same LEDs on and off for specific amounts of time. The top-left gif depicts a red LED blinking at 1 Hz. The middle gif of the top row shows a blue LED blinking at 10 Hz. Meanwhile, in the top-right, a yellow LED blinking at 50 Hz can be seen. The second row is the second idea that we explored in this lab. We were given amounts of time to keep the LEDs on and off. In the bottom-left, a red LED blinks with 1 second on and 100ms off. In the middle column of the bottom row, a blue LED stays on for 200ms and off for 50ms. In the bottom-right, a yellow LED staying on for 20ms and off for 10ms is depicted.

| ![Gif of Condition](Fig/c1_part1_a.gif) | ![Gif of Condition](Fig/c1_part1_b.gif) | ![Gif of Condition](Fig/c1_part1_c.gif) |
|----|----|----|
| ![Gif of Condition](Fig/c1_part2_a.gif) | ![Gif of Condition](Fig/c1_part2_b.gif) | ![Gif of Condition](Fig/c1_part2_c.gif) |


**Challenge 2** was an opportunity to explore debouncing buttons, if/else statements, and the digitalRead function. In this challenge, we were given the task of creating a stopwatch that starts when a button is pressed, and stops when it is pressed again, using the millis() function. In this project, we were faced with the challenge of debouncing, as initially, the timer would only work when the button is pressed. We had to implement a series of if-statements to ensure that the counter starts counting once the button is initially pressed, and stops the count completely when the button is pressed a second time. The gif below depicts the timer starting at zero, then a button initially being pressed to start the, then the button being pressed again to pause it.


![Gif of Condition](Fig/c2.gif)

**Challenge 3** allowed us to build upon our work from the previous challenge. Adding onto the previous code, we now initialize a variable that records the elapsed time to 0. Then, we have it increment by one every time the button is pushed. The timer starts to count down by one every second if the button hasn't been pushed in the previous three seconds, but it cannot go below zero. Below is an example in which the button is pressed, and the value of the timer is printed onto the serial monitor based on what is done to the button. One issue that was faced in this specific attempt, however, is that without visibly decrementing by one every second, the count would jump to zero three seconds after the button is last pushed.

![Gif of Condition](Fig/c3.gif)