import RPi.GPIO as GPIO
from time import sleep
from ultraModule import getDistance
from TurnModule import*
from go_any import*

GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)

def signal(n1, n2, n3, n4, n5):
    return A == n1 and B == n2 and C == n3 and D == n4 and E == n5



distance = getDistance()
list = [80, 0.5]
try:
    while True:
        A = GPIO.input(leftmostled)
        B = GPIO.input(leftlessled)
        C = GPIO.input(centerled)
        D = GPIO.input(rightlessled)
        E = GPIO.input(rightmostled)

        distance = getDistance()


        if signal(1, 1, 0, 1, 1) and distance > 20:
            go_forward_any(1, 1)

        elif signal(1, 0, 0, 1, 1) and distance > 20:
            go_forward_any(1, 1)

        elif signal(1, 1, 0, 0, 1) and distance > 20:
            go_forward_any(1, 1)

        elif signal(0, 0, 1, 1, 1) and distance > 20:
            lpt(3)

        elif signal(0, 1, 1, 1, 1) and distance > 20:
            lpt(6)

        elif signal(1, 1, 1, 0, 0) and distance > 20:
            rpt(3)

        elif signal(1, 1, 1, 0, 0) and distance > 20:
            rpt(6)

        elif signal(0, 0, 0, 0, 0) and distance > 20:
            stop()

        elif distance < 20:
            stop()
            sleep(3)
            rightSwingTurn(list)
            stop()
            sleep(3)






except KeyboardInterrupt:
    GPIO.cleanup()
