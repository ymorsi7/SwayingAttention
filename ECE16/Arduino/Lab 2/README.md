# ECE16 Lab 2 Report
Prepared by: Yusuf Morsi

Date: 02/01/2021

**Tutorial_DisplayI2C** is a tutorial in which we not only set up the OLED display,
but also install the correct libraries. In addition, we learn to write OLED functions
(which can be seen in this tutorial), and create multiple tabs in the same project
on Arduino IDE. Using both the "Wire.h" and the "U8x8lib" libraries, we create a 
program that prints information on different rows on the OLED display. In the code
for this, we utilize functions such as 'oled.print', 'delay,' for loops, 
if-statements, and more.

**Tutorial_AnalogInputPart1** teaches us how to set up an Accelerometer, read data from
it, and plot it with Arduino IDE's serial plotter. We use basic functions such as 'pinMode,' 'Serial.print,' and 'analogRead.'

**Tutorial_AnalogInputPart2** guides us to organizae and visualize the accelerometer. 
We first create a new tab for the Accelerometer, and define certain pins for it.
We then declare these three pins in the main tab and initialize them to zero.
After assigning the input pins as inputs, we store the readings of the pins, and 
plot them with Arduino IDE's serial plotter.

**Tutorial_AnalogOutputPart1** teaches us about PWM with Arduino IDE. We use the Sparkfun
ESP32's built-in LED to have it blink at a different frequency and resolution. We utilize
the functions 'ledcAttachPin()' and 'ledcWrite()' to both attatch the physical pin to the 
PWN chcannel, and set the duty cycle for the PWM channel. 

**Tutorial_AnalogOutputPart2** familiarizes us with the buzzer in our kit. We apply the
knowledge about PWM attained in the last part to our buzzer. After creating a new tab for
the motor, we set the PWM properties as global variables, define the frequency at 5KHz, the
channel as 0, and the resolution to be 8-bits. We create different functions for activating
and deactivating the motor, and program it to turn on and off in the main tab inside the
setup() and loop() functions. This teaches us to program the buzzer to buzz at different
intensities.

**Tutorial_Sampling** familiarizes us sampling with Arduino IDE. In addition to utilizing
the Accelerometer and Display tabs that we created earlier, we create a new one called
'Sampling.' After initializing our variables in the sampling tab, we create a bool function
that samples our sensors at the rate that we initialized at the top (to 50). We also create
another function called 'displaySampleRate()' that not only calculates the effective sampling
rate, but also prints it on the OLED. Subsequently, in the main tab, we add code that prints
the data. Our work allows us to see '50.00 Hz' displayed on the OLED, and the 3 acceloermeter
axes being plotted on the serial plotter.

**Challenge 1** teaches us to detect taps on the accelerometer and print how many times it
was tapped on the OLED. In this challenge, we not only plot the 3 axes of the accelerometer 
at 100 Hz, but we also observe the values that are passed when the accelerometer is tapped.
Using this information, we create a function that adds 1 to a variable initialized at zero, 
'numTaps,' every time the accelerometer is tapped. We also implement another function that
prints this value to the OLED. Both functions are then both called in the void loop() function.
Below is a gif of the OLED incrementing by one every time the accelerometer being tapped.
It is with both code and hardware that this detection is possible.

![Gif of Condition](Fig/c1.gif)

This image shows an accelerometer being tapped, causing the value on the OLED depicting the number of taps to increment by one every time.


**Challenge 2** was an opportunity to explore more applications to the topics we covered earlier in this lab. The goal of this is to use an accelerometer, motor, button, and OLED to detect every time the accelerometer is tapped and print it on the screen. In addition, the code is supposed to reset the count when the button is pushed down for more than two seconds, decrease the count by one for every second after it hasn't been pressed for four seconds (until it reaches zero), and to have the motor buzz every time the count is at zero. Although the final product could not be achieved, the motor was able to buzz based on the accelerometer's input.

 ![Jpg of Condition](Fig/c2_fsm.jpg) 

This is a finite state diagram of this challenge. Please note that it depicts that when the button is not tapped for four seconds, the count will go down by one for every second passed, but if a tap is detected, numTaps is increased by one. If the button is pushed for over two seconds, the numTaps variable is set to zero. When numTaps is zero, the motor buzzes. This whole time, the OLED is displaying the numTaps variable's value.

 ![Gif of Condition](Fig/c2.gif) |

This figure depicts an accelerometer being tapped and an OLED changing, while a buzzer is vibrating. Although this gif does not fully demonstrate the reset and countdown functionalities, it depicts communication between the code-base and circuit that causes the motor to buzz, and for the OLED to reflect the accelerometer's input.