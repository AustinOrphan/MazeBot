from initializeMotors import lMotors, rMotors

def fTravel(time=.25, power=50):
    lMotors.Forward(0,power/1.5)
    rMotors.Forward(0,power)
    lMotors.StopAfter(time)
    rMotors.Stop()
def rTravel(time=.25, power=50):
    lMotors.Backward(0,power/1.5)
    rMotors.Backward(0,power)
    lMotors.StopAfter(time)
    rMotors.Stop()
def rTurn(time=.7, power=100):
    lMotors.Forward(0,power/2)
    rMotors.Backward(0,power/2)
    lMotors.StopAfter(time)
    rMotors.Stop()
def lTurn(time=.7, power=100):
    rMotors.Forward(0,power/2)
    lMotors.Backward(0,power/2)
    rMotors.StopAfter(time)
    lMotors.Stop()
def fullTurn(time=1.75, power=100):
    lMotors.Forward(0,power/2)
    rMotors.Backward(0,power/2)
    lMotors.StopAfter(time)
    rMotors.Stop()
def fullStop():
    lMotors.Stop()
    rMotors.Stop()
