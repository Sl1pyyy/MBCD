import pyfirmata
import time

port = '/dev/ttyACM0'
board = pyfirmata.Arduino(port)

red_pin = 9
yellow_pin = 10
green_pin = 11

def all_off():
    board.digital[red_pin].write(0)
    board.digital[yellow_pin].write(0)
    board.digital[green_pin].write(0)

for i in range(5):
    #Red
    all_off()
    board.digital[red_pin].write(1)
    time.sleep(3)

    #Red and yellow
    all_off()
    board.digital[red_pin].write(1)
    board.digital[yellow_pin].write(1)
    time.sleep(3)

    #Green
    all_off()
    board.digital[green_pin].write(1)
    time.sleep(3)

    #Yellow
    all_off()
    board.digital[yellow_pin].write(1)
    time.sleep(2)
