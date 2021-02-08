# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:58:54 2021

@author: Yusuf Morsi
"""

import serial # the PySerial library
import time   # for timing purposes

def setup(serial_name, baud_rate):
    ser = serial.Serial(serial_name, baudrate=baud_rate)
    return ser

def close(ser):
    ser.close()

def main():
    ser = setup("COM3", 115200)
    close(ser)

"""
Main entrypoint for the application
"""
if __name__== "__main__":
    main()
    
def send_message(ser, message):
   if(message[-1] != '\n'):
       message = message + '\n'
   ser.write(message.encode('utf-8'))

def main():
    ser = setup("COM3", 115200)
    # time.sleep(3)
    send_message(ser, "hello world") # \n
    time.sleep(3)
    close(ser)

"""
Main entrypoint for the application
"""
if __name__== "__main__":
   main()
   
   
"""
Receive a message from Serial and limit it to num_bytes (default of 50)
"""
def receive_message(ser, num_bytes=50):
    if(ser.in_waiting > 0):
        return ser.readline(num_bytes).decode('utf-8')
    else:
        return None

def main():
    ser = setup("COM4", 115200)
    send_message(ser, "hello world\n")
    time.sleep(3)
    message = receive_message(ser)
    print(message)
    close(ser)

"""
Main entrypoint for the application
"""
if __name__== "__main__":
   main()