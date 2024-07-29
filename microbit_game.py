
from microbit import *
import time
import random
import sys

# Functions

# Reset Board: Clears all lights from the microbit display
def reset_board():
    display.show(Image('00000:'
                       '00000:'
                       '00000:'
                       '00000:'
                       '00000'))

# Setup

position = 2    # starting position for game (center of last row)
rand = random.randint(0, 4)    # random number between 0 and 4 inclusive
stone = -1    # starting position of stone (outside of screen)
page = 0    # starting page (menu page)

display.set_pixel(position, 4, 9)

display.show(Image.HEART)    # display a picture of a heart
time.sleep(1)    # let the heart image display for one second

# Loop

while True:    # begin loop

    while page == 0:    # while the user is in the menu
        
        display.show('M')    # display the letter M for menu for one second
        time.sleep(1)

        # display menu options
        display.show(Image('90000:'
                           '90000:'
                           '90000:'
                           '90000:'
                           '90000'))
        
        # get cursor ready
        menu_position = 0
        menu = True    # boolean that stays true until cursor selects an option
        
        while menu == True:    # while the user has not selected an option
            
            display.set_pixel(2, menu_position, 9)    # Set the cursor

            # if button a is pressed
            if button_a.was_pressed():
                if menu_position == 0:    # if the first option was selected
                    reset_board()         # reset the board and display a countdown
                    display.show('3') 
                    time.sleep(1)
                    display.show('2')
                    time.sleep(1)
                    display.show('1')
                    time.sleep(1)
                    display.show(Image('00000:'    # begin game display
                                       '00000:'
                                       '00000:'
                                       '00000:'
                                       '00900'))
                    time.sleep(1)    # give user one second to get ready
                    reset_board()    # reset the board
                    menu = False     # exit the menu
                    page = 1         # enter page 1 (the game)
                    
                if menu_position == 1:    # if the second option is selected
                    reset_board()     # reset the board
                    menu = False      # exit the menu
                    page = 2          # enter the second page (compass)
                    
            # scrolling functionality
            if button_b.was_pressed():    # if button B is pressed
                if menu_position < 4:  # if the cursor has not reached the bottom yet
                    display.set_pixel(2, menu_position, 0)  # hide the current pixel
                    menu_position = menu_position + 1       # set the new cursor position to the position below
                else:    # if the cursor has reached the bottom
                    display.set_pixel(2, menu_position, 0)  # hide the current pixel
                    menu_position = 0    # start the scrolling back from 0
            

    # option 1 (game)
    while page == 1:

        # stones dropping to the player
        if stone < 5:    # if the current stone position is less than 5
            stone = stone + 1    # make the stone go down by one pixel
            if stone == 5:    # once the stone reaches the bottom of the screen
                
                if rand == position:    # if the stone touches the player
                    position = 2    # reset the player
                    display.show(Image.SAD)    # display a sad face for one second
                    time.sleep(1)
                    display.show(Image('00000:'    # display two options, play again or quit
                                       '90000:'
                                       '00000:'
                                       '90000:'
                                       '00000'))
                    go_menu = True    # defines whether return to menu? page runs or not
                    go_menupos = 1    # start the cursor next to the first option
                    while go_menu == True:    # while the return to menu? page is running
                        display.set_pixel(2, go_menupos, 9)    # display the cursor two pixels to the right of the first option
                        if button_a.was_pressed():    # if button A is pressed
                            if go_menupos == 1:    # if the first option was selected
                                reset_board()
                                go_menu = False    # play the game again
                                page = 1
                            if go_menupos == 3:    # if the second option was selected
                                reset_board()
                                go_menu = False    # return to menu
                                page = 0
                                
                        # scrolling
                        if button_b.was_pressed():    # if button B was pressed
                            if go_menupos == 1:    # if the cursor position was 1, move it to position 3 
                                display.set_pixel(2, go_menupos, 0)
                                go_menupos = 3
                            else:                  # if the cursor position was 3, move it to 1
                                display.set_pixel(2, go_menupos, 0)
                                go_menupos = 1
                                
                display.set_pixel(rand, stone - 1, 0)    # if the stone did not fall on the player, reset it to a new random position and drop it again
                stone = -1
                rand = random.randint(0, 4)

            # dropping functionality
            elif stone == 0:    # if the stone is at the top of the screen
                display.set_pixel(rand, stone, 9)    # display it at the top of the screen in its random position
            elif stone > 0:     # if the stone is falling
                display.set_pixel(rand, stone - 1, 0)    # reset its previous position
                display.set_pixel(rand, stone, 9)        # set its new position

        # player location/moving
        display.set_pixel(position, 4, 0)    # set the player to its position in the bottom of the screen
    
        if button_a.was_pressed():    # if button A is pressed
            if position > 0:    # move the player position to the right unless the player has reached the very left side of the screen
                display.set_pixel(position, 4, 0)    # reset the previous position
                position = position - 1
                
            
        if button_b.was_pressed():    # if button B is pressed
            if position < 4:    # move the player position to the left unless the player has reached the very right side of the screen
                display.set_pixel(position, 4, 0)    # reset the previous position
                position = position + 1
    
        display.set_pixel(position, 4, 9)    # set the new position
            
        time.sleep(0.1)    # set a refresh rate of 10 frames per second

    # if the second page (compass) was selected
    while page == 2:    # enter the compass page
        if(compass.is_calibrated() == False):    # calibrate the compass if necessary
            compass.calibrate()
        oncompass = True    # set a boolean to stay on the compass page
        while(compass.is_calibrated() and oncompass):    # compass loop
            # display first letter of direction faced with 90 degree range [direction - 45, direction + 45)
            if(compass.heading() >= 315 or compass.heading() < 45):
                display.show('N')
            elif(compass.heading() >= 45 and compass.heading() < 135):
                display.show('E')
            elif(compass.heading() >= 135 and compass.heading() < 225):
                display.show('S')
            elif(compass.heading() >= 225 and compass.heading() < 315):
                display.show('W')
            if(button_a.was_pressed() or button_b.was_pressed()):    # if any button is pressed
                oncompass = False    # quit the calculator
                page = 0             # re-enter the menu
            
                
        
        
    
    
    
