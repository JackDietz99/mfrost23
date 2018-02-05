import setup
import RoboPiLib as RPL
import time

timer = time.time()
close = RPL.digitalRead(16)
motorL = 1
motorR = 2

RPL.servoWrite(motorL, x)

while True:
    while RPL.digitalRead(16) == 0:
        while timer < 5:
            RPL.servoWrite(motorR, 100)
            RPL.servoWrite(motorL, 1600)
        while timer >= 5:
            RPL.servoWrite(motorL, 0)
            RPL.servoWrite(motorR, 0)
    while RPL.digitalRead(16) == 1:
        RPL.servoWrite(motorL, 1000)
        RPL.servoWrite(motorR, 2000)
