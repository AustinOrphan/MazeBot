import curses
from initializeMotors import lMotors, rMotors

def F():
    lMotors.Forward()
    rMotors.Forward()

def B():
    lMotors.Backward()
    rMotors.Backward()

def L():
    lMotors.Backward()
    rMotors.Forward()

def R():
    lMotors.Forward()
    rMotors.Backward()

actions = {
    curses.KEY_UP:    F,
    curses.KEY_DOWN:  B,
    curses.KEY_LEFT:  L,
    curses.KEY_RIGHT: R,
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            lMotors.Stop()
            rMotors.Stop()

curses.wrapper(main)
