# ECE16 Lab 3 Report
Prepared by: Yusuf Morsi

Date: 02/07/2021

**Tutorial Pyserial** begins by leading us through the process of installing 'pyserial.' After importing both 'serial' and 'time' at the top of the file, we learn to connect our Arduino to the Python file. Subsequent to creating functions that allow us to send and recieve data with the MCU and close the Serial Port, we work with programming our OLED with Python. We write code in the Arduino IDE for initializing the communication protocol and sending and recieving messages. Subsequently, we set up Bluetooth communication by creating and naming a port in our Arduino code. After this, we enter our computer's settings to connect the device, and after it connects, we make a few changes in our Python code to get our output printed on the OLED through the Sparkfun ESP32!

**Challenge 2: Weather Watch** brings us into the world of real-life applications of our given technology. After first installing PyOWM and activating the API key, we import PyOWM in out Python file and instantiate a OWM object to gain the information that we need (local time and weather). Using the technology we explored in the previous challenge and tutorials, we display the current time, date, and weather on our OLED. In addition, we regulate the OLED display refresh rate and send data from Python at once a second in order to have the display updated once a second. We needed to create an Arduino file to send the data to the OLED using the Sparkfun board, which is technology that we learned about in Lab 2.

The submitted gif shows an OLED displaying the current time, the current data, and the current weather based on the code creating with PyOWM.


