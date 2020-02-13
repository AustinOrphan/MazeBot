from navigation import *
from ExternalStateServo import *
import RPi.GPIO as GPIO
import sys
def peek(stack):
    if stack == []:
        return None
    else:
        return stack[-1]    # this will get the last element of stack

def count(stack, obj):
    c = 0
    for s in stack:
        if s == obj:
            c += 1
    print(obj + "Count: " + str(c))
    return c

def followWall(stayThisClose, newDist, di):
    if newDist > stayThisClose+3:
        turn = "toward"
    elif newDist < stayThisClose-3:
        turn = "away"
    else:
        turn = None
    return turn


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ambientTemp = getTemp()
pFDist = 0
travelled = []
read = []
justLeft = False
actions = []
lDist = []
fDist = []
rDist = []
adjusted = True
try:
    while True:
        temp = getTemp()
        light = getLight()
        if temp > ambientTemp + 5 and peek(actions) != "h":
            print("Too hot! Turning around.")
            fullTurn()
            actions.append("h")
        elif not light and peek(actions) != "d":
            print(light)
            print("Too dark! Turning around.")
            fullTurn()
            actions.append("d")
        else:
            distances = getDistances()
            lDist.append(distances[0])
            print(peek(lDist))
            fDist.append(distances[1])
            print(peek(fDist))
            rDist.append(distances[2])
            print(peek(rDist))

            if peek(lDist) > 30 and peek(actions) != "l" and (count(actions, "l")==0 or (count(actions, "r")==2 and count(actions, "l") < 2 )):
                print("Louie!")
                lTurn()
                actions.append("l")
            elif peek(fDist) > 8:
                print("Onward!")
                if peek(actions) != "f":
                    if peek(lDist)<peek(rDist):
                        di = "l"
                        stayThisClose = peek(lDist)
                    else:
                        di = "r"
                        stayThisClose = peek(rDist)
                if followWall(stayThisClose, peek(lDist), "l") == None or adjusted == True:
                    fTravel(peek(fDist)/30)
                    adjusted = False
                else:
                    adjusted = True
                    if di == "l":
                        if followWall(stayThisClose, peek(lDist), "l") == "toward":
                            lTurn(.1)
                        elif followWall(stayThisClose, peek(lDist), "l") == "away":
                            rTurn(.1)
                    elif di == "r":
                        if followWall(stayThisClose, peek(rDist), "r") == "toward":
                            rTurn(.1)
                        elif followWall(stayThisClose, peek(lDist), "r") == "away":
                            lTurn(.1)

                # print(fDist)
                # if pFDist>0:
                #     travDist = pFDist - fDist
                #     print("Travelled: " + str(travDist) + " inches")
                #     travelled.append(travDist)
                #     read.append(fDist)
                # pFDist = fDist
                actions.append("f")
            elif peek(rDist) > 16 and peek(actions) != "r" and count(actions, "r") < 2  and count(actions, "l") >0:
                print("Ralph!")
                rTurn()
                actions.append("r")
            elif peek(actions) != "b":
                print("I am stuck! Let's back it up.")
                rTravel()
                actions.append("b")
except KeyboardInterrupt:
    GPIO.cleanup()
    print"Bye-bye!"
    # print(travelled)
    # print(read)
    # shoulda = []
    # for r in travelled:
    #     shoulda.append(r/80)
    # print(shoulda)
    # rat = []
    # i=0
    # for s in shoulda:
    #     ratio = travelled[i]/s
    #     rat.append(ratio)
    #     print(rat[i])
    #     i+=1
    # print(rat)
    # summ = 0
    # i = 0
    # for ra in rat:
    #     summ += ra
    #     i += 1
    # print summ/i
    sys.exit(0)

