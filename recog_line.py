
# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

# =======================================================================
#  leftL2    leftL1     center     rightL1     rightL2
#   16         18         22         40           32
# =======================================================================

L2 = 16 #1
L1 = 18 #2
C = 22 #3
R1 = 40 #4
R2 = 32 #5

#========================================================================
# setup - senser
#========================================================================

GPIO.setup(L2, GPIO.IN)
GPIO.setup(L1, GPIO.IN)
GPIO.setup(C, GPIO.IN)
GPIO.setup(R1, GPIO.IN)
GPIO.setup(R2, GPIO.IN)

def led():
    A = GPIO.input(L2)
    B = GPIO.input(L1)
    C = GPIO.input(C)
    D = GPIO.input(R1)
    D = GPIO.input(R2)

    led_sig = [A, B, C, D, E]
    return led_sig

case_led = {"straight": [[1,1,0,1,1], [1,0,0,1,1], [1,1,0,0,1]],
            "left" : [[0,1,1,1,1], [0,0,1,1,1],[1,0,1,1,1]],
            "right" : [[1,1,1,1,0], [1,1,1,0,0],[1,1,1,0,1]],
            "right turn": [[0,0,0,0,0], [1,1,0,0,0], [1,0,0,0,0]],
            }

def status(led_sig) :

    if led_sig in case_led["straight"]:
        stat = "inLine"

    elif led_sig in case_led["left"]:
        stat = "left"

    elif led_sig in case_led["right"]:
        stat ="right"

    elif led_sig in case_led["right turn"]:
        stat = "right turn"

    elif led_sig == [0,0,0,1,1] :
        stat = "left or straight"

    elif led_sig == [1,1,1,1,1] :
        stat = "Uturn"

    else:
        stat = "???"

    return stat
