import RPi.GPIO as GPIO
from time import sleep
from ultraModule import *
from TurnModule import *
from go_any import *
from trackingModule import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


def signal(n1, n2, n3, n4, n5):
    return A == n1 and B == n2 and C == n3 and D == n4 and E == n5




list = [80, 0.5]
try:
    while True:
        A = GPIO.input(leftmostled)
        B = GPIO.input(leftlessled)
        C = GPIO.input(centerled)
        D = GPIO.input(rightlessled)
        E = GPIO.input(rightmostled)
       
	distance = getDistance() 
        print(distance)
                
        if signal(1, 1, 0, 1, 1):
            go_forward_any(1, 1)
	    print(1)

        elif signal(1, 0, 0, 1, 1):
            go_forward_any(1, 1)
	    print(2)

        elif signal(1, 1, 0, 0, 1):
	    print(3)
            go_forward_any(1, 1)

        elif signal(0, 0, 1, 1, 1):
	    print(4)
            lpt(2)

        elif signal(0, 1, 1, 1, 1):
	    print(5)
            lpt(4)

        elif signal(1, 1, 1, 0, 0):
	    print(6)
            rpt(2)

        elif signal(1, 1, 1, 1, 0):
	    print(7)
            rpt(4)

        elif signal(0, 0, 0, 0, 0):
	    print(8)
            stop()

	elif distance < 20:
           #print("distance")
	   #stop()
	   #GPIO.cleanup()
	   #break
           rightPointTurn(10, 0.5)
	   stop()
	   sleep(1)
           go_forward(20, 5)
 	   stop()
	   sleep(1)
           leftPointTurn(10, 0.5)




except KeyboardInterrupt:
    print('key')
    pwm_low()

