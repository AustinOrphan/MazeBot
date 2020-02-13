from Actuators import AdjMotor
import sys
import RPi.GPIO as GPIO
LAdjMotor = AdjMotor.AdjMotor(22,27)
LAdjMotor.Forward(1,20)
GPIO.cleanup()
