from time import sleep
from TurnModule import *
from go_any import *
import recog_line


def signal():
    status = recog_line.led()
    print(status)
    return recog_line.status(status)

def maze(line):
    if line == "inLine":
        go_forward_any(1, 1)

    elif line == "right":
        rpt(2)

    elif line == "left":
        lpt(2)

    elif line == "right turn":
        print("rightTurn")
        go_forward(1, 0.085)
        stop()
        sleep(0.5)
        rightPointTurn(30, 0.32)
        stop()
        sleep(0.5)
        status = recog_line.led()
        while status[2] != 0:
            rpt(2)
            status = recog_line.led()
        else:
            leftPointTurn(30, 0.2)

    elif line == "Uturn":
        print("Uturn")
        go_forward(1, 0.23)
        stop()
        sleep(0.5)
        rightPointTurn(30, 0.72)
        stop()
        sleep(0.5)
        status = recog_line.led()
        while status[2] != 0:
            rpt(0.01)
            status = recog_line.led()
        else:
            leftPointTurn(30, 0.23)
            status = recog_line.led()
            while status[2] != 0:
                lpt(0.1)
                status = recog_line.led()

    elif line == "left or straight":
        print("left")
        go_forward(1, 0.24)
        stop()
        sleep(0.5)
        status = recog_line.led()
        if status == [1, 1, 1, 1, 1]:
            lpt(1)
            sleep(0.05)
            stop()
            sleep(1)
            status = recog_line.led()
            while status[2] != 0:
                lpt(1)
                sleep(0.04)
                stop()
                sleep(0.1)
                status = recog_line.led()
            else:
                stop()
                sleep(1)
                status = recog_line.led()
                if status[2] != 0:
                    rpt(1)
                    status = recog_line.led()

                elif status == [1, 1, 0, 1, 1]:
                    pass
    else:
        pass

