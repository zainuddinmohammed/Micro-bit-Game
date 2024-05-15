
from microbit import *
import time
import random
import sys

# Functions

def reset_board():
    display.show(Image('00000:'
                       '00000:'
                       '00000:'
                       '00000:'
                       '00000'))

# Setup

position = 2
rand = random.randint(0, 4)
stone = -1

display.set_pixel(position, 4, 9)

# Loop
while True:

    if stone < 5:
        stone = stone + 1
        if stone == 5:
            
            if rand == position:
                display.show(Image.SAD)
                display.scroll('Time:')
                display.scroll((running_time() - 5000)/1000)
                display.scroll('Try Again!')
                display.show(Image.CLOCK12)
                time.sleep(0.1)
                display.show(Image.CLOCK1)
                time.sleep(0.05)
                display.show(Image.CLOCK2)
                time.sleep(0.05)
                display.show(Image.CLOCK3)
                time.sleep(0.05)
                display.show(Image.CLOCK4)
                time.sleep(0.05)
                display.show(Image.CLOCK5)
                time.sleep(0.05)
                display.show(Image.CLOCK6)
                time.sleep(0.05)
                display.show(Image.CLOCK7)
                time.sleep(0.05)
                display.show(Image.CLOCK8)
                time.sleep(0.05)
                display.show(Image.CLOCK9)
                time.sleep(0.05)
                display.show(Image.CLOCK10)
                time.sleep(0.05)
                display.show(Image.CLOCK11)
                time.sleep(0.05)
                display.show(Image.CLOCK12)
                time.sleep(0.5)
                reset_board()
                sys.exit()
            display.set_pixel(rand, stone - 1, 0)
            stone = -1
            rand = random.randint(0, 4)
        elif stone == 0:
            display.set_pixel(rand, stone, 9)
        elif stone > 0:
            display.set_pixel(rand, stone - 1, 0)
            display.set_pixel(rand, stone, 9)

    display.set_pixel(position, 4, 0)

    if button_a.was_pressed():
        if position > 0:
            display.set_pixel(position, 4, 0)
            position = position - 1
            
        
    if button_b.was_pressed():
        if position < 4:
            display.set_pixel(position, 4, 0)
            position = position + 1

    display.set_pixel(position, 4, 9)
        
    time.sleep(0.1)
        
    
    
    