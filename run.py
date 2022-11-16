import os
from random import randint
import numpy as np
from getkey import getkey, keys

graphic_ocean = np.array([
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"],
    ["~", "~", "~", "~", "~"]])

hidden_ocean = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])

cursor_x = 2
cursor_y = 2
turns = 0
hit_miss = ""
hit_boats = 0
difficulty = 0


def logo():
    '''
    This function creates a logo.
    '''
    stars = "************"
    star_line = "**************************************"

    os.system('clear')
    print(star_line)
    print(stars, "BATTLEBOATS!", stars)
    print(star_line)


def game_stats():
    '''
    This function shows graphic reminders and gameplay stats.
    '''
    print("Use Arrow keys to navigate \nUse Space key to shoot\n")
    print("Sight: +")
    print("Water: ~")
    print("Miss:  O")
    print("Hit:   X  \n")
    print("Turn: ", turns, "/", difficulty)
    print("Hit Boats: ", hit_boats)
    print("Hit or Miss: ", hit_miss, "\n")


def draw_graphics():
    '''
    This function creates and updates graphic
    '''
    for y in range(5):
        for x in range(5):
            if hidden_ocean[x, y] == 0:
                graphic_ocean[x, y] = "~"
            elif hidden_ocean[x, y] == 1:
                graphic_ocean[x, y] = "~" 
            elif hidden_ocean[x, y] == 2:
                graphic_ocean[x, y] = "X"
            elif hidden_ocean[x, y] == 3:
                graphic_ocean[x, y] = "O" 
    if turns != difficulty and hit_boats != 5:
        graphic_ocean[cursor_x, cursor_y] = "+"
    for y in range(5):
        for x in range(5):
            print(graphic_ocean[x, y], end=" ")
        print("")
    if hit_boats == 5 or turns == difficulty:
        if hit_boats == 5:
            print("\n Congratulations you won !")
        else:
            print("\n You Lost !")
        print("\n Press Enter.")


def spawn_boats():
    '''
    This function places five boats randomly in hidden_ocean
    '''
    for boats in range(5):
        boat_x, boat_y = randint(0, 4), randint(0, 4)
        while hidden_ocean[boat_x][boat_y] == 1:
            boat_x, boat_y = randint(0, 4), randint(0, 4)
        hidden_ocean[boat_x][boat_y] = 1


def reset():
    '''
    This function resets the variables and hidden_ocean
    '''
    global cursor_x
    global cursor_y
    global turns
    global hit_boats
    global hit_miss
    
    cursor_x = 2
    cursor_y = 2
    turns = 0
    hit_boats = 0
    hit_miss = ""

    for y in range(5):
        for x in range(5):
            hidden_ocean[x, y] = 0
    spawn_boats()


def start_program():
    '''
    This function contains the gameplay controls,
    tells player when they hit wrong buttons,
    adds to turns, tells player when they hit or miss,
    stops gameplay when 5 boats are hit or when turns reach difficulty,
    What the numbers mean in hidden_ocean:
    Hidden Water = 0
    Hidden Boats = 1
    Shot boat = 2
    Shot water = 3
    '''
    global cursor_x
    global cursor_y
    global turns
    global hit_boats
    global hit_miss

    while (True):
        main_menu()
        while (turns < difficulty):       
            # Controls
            clicked_button = getkey()
            if clicked_button == keys.RIGHT and cursor_x + 1 != 5:
                cursor_x += 1    
            elif clicked_button == keys.DOWN and cursor_y + 1 != 5:
                cursor_y += 1      
            elif clicked_button == keys.LEFT and cursor_x - 1 != -1:
                cursor_x -= 1      
            elif clicked_button == keys.UP and cursor_y - 1 != -1:
                cursor_y -= 1      
            elif clicked_button == keys.SPACE: 
                # Update graphics in hidden_ocean
                if hidden_ocean[cursor_x, cursor_y] < 2:
                    turns += 1
                else:
                    hit_miss = "you already shot there!"   
                if hidden_ocean[cursor_x, cursor_y] == 0:
                    hidden_ocean[cursor_x, cursor_y] = 3
                    graphic_ocean[cursor_x, cursor_y] = "O"
                    hit_miss = "you Missed !!"                        
                elif hidden_ocean[cursor_x, cursor_y] == 1:
                    hidden_ocean[cursor_x, cursor_y] = 2
                    graphic_ocean[cursor_x, cursor_y] = "X"
                    hit_miss = "you hit a boat!"
                    hit_boats += 1
            # Test for wrong buttonclicks
            else:
                hit_miss = "Use Arrow keys or Space key instead!"           
            logo()
            game_stats()
            draw_graphics()
            if hit_boats == 5 or turns == difficulty:
                while (True):
                    key_pressed = getkey()
                    if key_pressed == keys.ENTER:
                        break
                break
            hit_miss = ""


def rule_book():
    '''
    This function just tell player what the rules are
    '''
    os.system('clear')
    print("Use Arrow keys to navigate \nUse Space key to shoot\n")
    print("Sight: +")
    print("Water: ~")
    print("Miss:  O")
    print("Hit:   X  \n")
    print("Easy Mode: 15 turns")
    print("Hard Mode: 10 turns \n")
    print("Boats are 1 square large \n")
    print("Navigate with Arrow keys on keyboard")
    print("Shoot with Space key on keyboard \n")
    print("Objective: Defeat all 5 enemy boats to win \n\n")
    input("Press Enter to go back to Menu\n")


def start_game():
    '''
    This function starts the game
    '''
    os.system('clear')
    reset()
    logo()
    game_stats()
    draw_graphics()
    spawn_boats()


def main_menu():
    '''
    This function contains the main menu 
    '''
    option = [
        "Easy Mode",
        "Hard Mode",
        "Rule Book", ]
    choice = 0
    while (True):
        os.system('clear')
        logo()
        print("Use Arrow keys to navigate \nUse Enter key to select\n")
        if choice == 0:
            print(">", option[0], "<")
            print(" ", option[1])
            print(" ", option[2])  
        elif choice == 1:
            print(" ", option[0])
            print(">", option[1], "<")
            print(" ", option[2])
        elif choice == 2:
            print(" ", option[0])
            print(" ", option[1])
            print(">", option[2], "<")
        key_pressed = getkey()
        if key_pressed == keys.DOWN and choice + 1 != len(option):
            choice += 1
        elif key_pressed == keys.UP and choice >= 1:
            choice -= 1
        elif key_pressed == keys.ENTER:
            global cursor_x
            global cursor_y
            global difficulty
            global turns
            global hit_boats
            global hit_miss
            global play_again
            cursor_x = 2
            cursor_y = 2
            turns = 0
            hit_boats = 0
            hit_miss = ""
            if choice == 0:
                # Easy mode
                difficulty = 15
                start_game()
                break
            elif choice == 1:
                # Hard mode
                difficulty = 10
                start_game()
                break
            elif choice == 2:
                # Rule book
                rule_book()


start_program()
