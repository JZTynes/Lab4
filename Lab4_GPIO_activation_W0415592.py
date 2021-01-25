""" /**************************************************
Lab #4 Program
Title: Basic GPIO activation
Student: Joshua Z. Tynes
Student #: W0415592
Instructor: Ricardo Bautista Quintero
Date:January 25th 2021
NSCC Ivany Campus
/**************************************************"""
"""

In this Lab, we will demonstrate how to blink an LED
connected to a General Purpose Input Output pin using:

1.) Pin distribution map
2.) Pin assignment
3.) for loop
4.) library import
5.) led.on
6.) led.off
7.) sleep(t)

"""
from gpiozero import LED #import LED module
from time import sleep #import sleep module

def Lab4():
  p1 = 21
  led = LED(p1)
  loop = 10
  t = 1 #time in seconds to sleep
  
  # loop 10 times
  for i in range(loop):
      print("Iteration", end=" ")
      print(i+1)
      print()
      led.on() #turn led on
      print("LED", end=" ")
      print(p1, end=" ")
      print("is on for", end=" ")
      print(t, end=" ")
      print("second.")
      sleep(t) #sleep for t seconds
      led.off #turn led off
      print("LED", end=" ")
      print(p1, end=" ")
      print("is off for", end=" ")
      print(t, end=" ")
      print("second.")
      sleep(t) #sleep for t seconds
      print()
if __name__ == '__main__':
  Lab4()