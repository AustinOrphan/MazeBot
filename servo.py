import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

servoData = 14
degrees = 0
sleepTime = .01

GPIO.setup(servoData, GPIO.OUT)

p = GPIO.PWM(servoData, 50)

dutyCycle = ((degrees)/18) + 2

p.start(7.5)

p.ChangeDutyCycle(12.5)  # turn towards 90 degree
time.sleep(1) # sleep 1 second
p.ChangeDutyCycle(7.5)  # turn towards 0 degree
time.sleep(1) # sleep 1 second
p.ChangeDutyCycle(2.5) # turn towards 180 degree
time.sleep(1) # sleep 1 second

try:
    while True:
        while degrees < 100:
            print degrees
            dutyCycle = ((degrees)/18) + 7.5
            p.ChangeDutyCycle(dutyCycle)  # turn towards 90 degree
            time.sleep(sleepTime) # sleep 1 second
            degrees += 1
        while degrees > -100:
            print degrees
            dutyCycle = ((degrees)/18) + 7.5
            p.ChangeDutyCycle(dutyCycle)  # turn towards 90 degree
            time.sleep(sleepTime) # sleep 1 second
            degrees -= 1
        dutyCycle = ((0)/18) + 7.2
        p.ChangeDutyCycle(dutyCycle)
        time.sleep(2)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()


