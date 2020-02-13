import sys
import time
import RPi.GPIO as GPIO
from Sensors import Distance
from Effectors import Wheels
GPIO.cleanup()
lForward=24
lBackward=23
rForward=27
rBackward=22
sleeptime=.01

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

rDS = Distance.Distance(5,6)
goodRead = False
maxDistance = 60
reads = []
reads.append(maxDistance + 1)
while not goodRead:
    rDS.Measure()
    reads[0] = rDS.inches
    if reads[0] < maxDistance:
        goodRead = True

cycle = 1
rightsInARow = 0
leftsInARow = 0
try:
    while True:
        goodRead = False
        i = 0
        while not goodRead:
            rDS.Measure()
            read = rDS.inches
            i += 1
            if read < maxDistance:
                goodRead = True
            elif i > 10:
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(lForward, GPIO.OUT)
                GPIO.setup(lBackward, GPIO.OUT)
                GPIO.setup(rForward, GPIO.OUT)
                GPIO.setup(rBackward, GPIO.OUT)
                forward(sleeptime)
        reads.append(read)

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(lForward, GPIO.OUT)
        GPIO.setup(lBackward, GPIO.OUT)
        GPIO.setup(rForward, GPIO.OUT)
        GPIO.setup(rBackward, GPIO.OUT)


        if leftsInARow > 3: # or reads[cycle] < reads[cycle-10]: # if closer to the wall now than three measurements ago, turn to the left a bit
            rforward(sleeptime*3)
            leftsInARow = 0
        elif rightsInARow > 3: # or reads[cycle] > reads[cycle-10]:
            lforward(sleeptime*3)
            rightsInARow = 0

        if reads[cycle] < reads[0]-3:  # rotates left
            rforward(sleeptime)
            forward(sleeptime*2)
            lforward(sleeptime)
            leftsInARow+=1

        elif reads[cycle] > reads[0]+3: # rotates right
            lforward(sleeptime)
            forward(sleeptime*2)
            rforward(sleeptime)
            rightsInARow+=1

        else:
            forward(sleeptime)
        GPIO.cleanup
        cycle+=1
except(KeyboardInterrupt):
    GPIO.cleanup()
    print"Bye-bye!"




# while (i<5):

#     rforward(sleeptime)
#     rreverse(sleeptime)

#     lforward(sleeptime)
#     lreverse(sleeptime)

#     #forward(1)
#     #reverse(1)

#     i+=1

GPIO.cleanup()
