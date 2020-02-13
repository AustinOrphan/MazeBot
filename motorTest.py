import sys
import time
import RPi.GPIO as GPIO

lForward=22
lBackward=27
rForward=23
rBackward=24
sleeptime=1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(lForward, GPIO.OUT)
GPIO.setup(lBackward, GPIO.OUT)
GPIO.setup(rForward, GPIO.OUT)
GPIO.setup(rBackward, GPIO.OUT)
i=0

def rforward(x):
	GPIO.output(rForward, GPIO.HIGH)
	print("Right Moving Forward")
	time.sleep(x)
	GPIO.output(rForward, GPIO.LOW)

def rreverse(x):
	GPIO.output(rBackward, GPIO.HIGH)
	print("Right Moving Backward")
	time.sleep(x)
	GPIO.output(rBackward, GPIO.LOW)

def lforward(x):
	GPIO.output(lForward, GPIO.HIGH)
	print("Left Moving Forward")
	time.sleep(x)
	GPIO.output(lForward, GPIO.LOW)

def lreverse(x):
	GPIO.output(lBackward, GPIO.HIGH)
	print("Left Moving Backward")
	time.sleep(x)
	GPIO.output(lBackward, GPIO.LOW)

def forward(x):
	GPIO.output(rForward, GPIO.HIGH)
	GPIO.output(lForward, GPIO.HIGH)
        print("Moving Forward")
        time.sleep(x)
        GPIO.output(rForward, GPIO.LOW)
        GPIO.output(lForward, GPIO.LOW)

def reverse(x):
	GPIO.output(rBackward, GPIO.HIGH)
        GPIO.output(lBackward, GPIO.HIGH)
        print("Moving Backward")
        time.sleep(x)
        GPIO.output(rBackward, GPIO.LOW)
        GPIO.output(lBackward, GPIO.LOW)

while (i<5):

	rforward(.1)
	rreverse(.1)

	lforward(.1)
	lreverse(.1)

	#forward(1)
	#reverse(1)

	i+=1

GPIO.cleanup()
