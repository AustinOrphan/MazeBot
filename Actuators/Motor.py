import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
defPower = 100

class Motor:
    def __init__(self, forwardPin, backwardPin):
        self.forwardPin = forwardPin
        self.backwardPin = backwardPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(forwardPin, GPIO.OUT)
        GPIO.setup(backwardPin, GPIO.OUT)

    def Forward(self, onTime=0, power=defPower):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.forwardPin, GPIO.OUT)
        self.pwm=GPIO.PWM(self.forwardPin,100)
        self.pwm.start(power)
        if onTime != 0:
            self.StopAfter(onTime)

    def Backward(self, onTime=0, power=defPower):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.backwardPin, GPIO.OUT)
        self.pwm=GPIO.PWM(self.backwardPin,100)
        self.pwm.start(power)
        if onTime != 0:
            self.StopAfter(onTime)

    def Stop(self):
        self.pwm.stop()

    def StopAfter(self, waitTime):
        time.sleep(waitTime)
        self.Stop()
