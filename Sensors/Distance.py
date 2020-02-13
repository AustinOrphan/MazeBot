class Distance:
    def __init__(self, TRIG, ECHO):
        self.TRIG = TRIG
        self.ECHO = ECHO

    def Measure(self):
        import RPi.GPIO as GPIO
        import time
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)
        TRIG = self.TRIG
        ECHO = self.ECHO

        # print "Distance Measurement in Progress"

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)



        pulse_start = -1
        pulse_end = -1

        while pulse_start == -1 or pulse_end == -1:
            pulse_start = -1
            pulse_end = -1
            GPIO.output(TRIG, False)
            # print "Waiting for Sensor to Settle"
            time.sleep(.0001)
            # print "Before pulse_start"
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            # loopCount=0
            while GPIO.input(ECHO)==0:
                pulse_start = time.time()
            #     loopCount+=1
            #     if loopCount > 500000:
            #         break
            # loopCount=0

            while GPIO.input(ECHO)==1:
                pulse_end = time.time()
                # loopCount+=1
                # if loopCount > 500000:
                #     break

        pulse_duration = pulse_end - pulse_start

        centimeters = pulse_duration * 17150
        inches = centimeters * 0.393701

        self.centimeters = round(centimeters, 2)
        # print "Distance in centimeters: ", centimeters, "cm"

        inches = round(inches, 2)
        # print "Distance in inches: ", inches, "in"

        GPIO.cleanup()
        self.inches = inches


