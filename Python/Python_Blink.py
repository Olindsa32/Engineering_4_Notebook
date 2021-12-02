# Python Program - Blink (ENG4)
# Written by Owen Lindsay
# 11/29/21
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM) # this sets my pin numbering scheme as the BCM
GPIO.setup(16,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
while True:
	print ("GREEN ON")
	GPIO.output(21,True)
	print ("RED OFF")
	GPIO.output(16,False)
	sleep(.5)
	print ("GREEN OFF")
	GPIO.output(21,False)
	print ("RED OFF")
	GPIO.output(16,True)
	sleep(.5)
