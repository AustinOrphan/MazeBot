class Light:
    def __init__(self, PIN):
        self.PIN = PIN

    def Measure(self):
        import RPi.GPIO as GPIO
        GPIO.setwarnings(False)
        GPIO.cleanup()
        # import time
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.PIN,GPIO.IN)
        level = 0
        try:
            count=0
            while(count<5):
                # print(GPIO.input(self.PIN))
                if(GPIO.input(self.PIN) == 1):
                    # print("\nLight detected")
                    level+=1
                    count+=1
                else:
                    # print("\nLight not detected")
                    count+=1

                # time.sleep(.1)
            # print(level)
            # print(count)
            level = float(level)/count
            # print(level)
        finally:
            GPIO.cleanup()
            print("Light level: ", level)
            return level
            # time.sleep(2)


