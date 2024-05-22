
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
page = 0

display.set_pixel(position, 4, 9)

# Loop

display.show(Image.HEART)
time.sleep(1)

while True:

    while page == 0:
        
        display.show('M')
        time.sleep(1)
        display.show(Image('90000:'
                           '90000:'
                           '90000:'
                           '90000:'
                           '90000'))
        menu_position = 0
        menu = True
        
        while menu == True:
            
            display.set_pixel(2, menu_position, 9)
            
            if button_a.was_pressed():
                if menu_position == 0:
                    reset_board()
                    display.show('3')
                    time.sleep(1)
                    display.show('2')
                    time.sleep(1)
                    display.show('1')
                    time.sleep(1)
                    display.show(Image('00000:'
                                       '00000:'
                                       '00000:'
                                       '00000:'
                                       '00900'))
                    time.sleep(1)
                    reset_board()
                    menu = False
                    page = 1
                if menu_position == 1:
                    reset_board()
                    menu = False
                    page = 2
                    
                
            if button_b.was_pressed():
                if menu_position < 4:
                    display.set_pixel(2, menu_position, 0)
                    menu_position = menu_position + 1
                else:
                    display.set_pixel(2, menu_position, 0)
                    menu_position = 0
            

    while page == 1:
        if stone < 5:
            stone = stone + 1
            if stone == 5:
                
                if rand == position:
                    position = 2
                    display.show(Image.SAD)
                    time.sleep(1)
                    display.show(Image('00000:'
                                       '90000:'
                                       '00000:'
                                       '90000:'
                                       '00000'))
                    go_menu = True
                    go_menupos = 1
                    while go_menu == True:
                        display.set_pixel(2, go_menupos, 9)
                        if button_a.was_pressed():
                            if go_menupos == 1:
                                reset_board()
                                go_menu = False
                                page = 1
                            if go_menupos == 3:
                                reset_board()
                                go_menu = False
                                page = 0
                                
                            
                        if button_b.was_pressed():
                            if go_menupos == 1:
                                display.set_pixel(2, go_menupos, 0)
                                go_menupos = 3
                            else:
                                display.set_pixel(2, go_menupos, 0)
                                go_menupos = 1
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

    while page == 2:
        if(compass.is_calibrated() == False):
            compass.calibrate()
        oncompass = True
        while(compass.is_calibrated() and oncompass):
            if(compass.heading() >= 315 or compass.heading() < 45):
                display.show('N')
            elif(compass.heading() >= 45 and compass.heading() < 135):
                display.show('E')
            elif(compass.heading() >= 135 and compass.heading() < 225):
                display.show('S')
            elif(compass.heading() >= 225 and compass.heading() < 315):
                display.show('W')
            if(button_a.was_pressed() or button_b.was_pressed()):
                oncompass = False
                page = 0
            
                
        
        
    
    
    
