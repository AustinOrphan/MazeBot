import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class AdjMotor:
    def __init__(self, forwardPin, backwardPin):
        self.forwardPin = forwardPin
        self.backwardPin = backwardPin
        GPIO.setup(forwardPin, GPIO.OUT)
        GPIO.setup(backwardPin, GPIO.OUT)

    def Forward(self, onTime, power):
        fpwm=GPIO.PWM(self.forwardPin,100)
        fpwm.start(power)
        time.sleep(onTime)
        fpwm.stop()

    def Backward(self, onTime, power):
        bpwm=GPIO.PWM(self.reversePin,100)
        bpwm.start(power)
        time.sleep(onTime)
        bpwm.stop()
