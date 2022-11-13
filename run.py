# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
    stars = "**********"
    star_line = "**********************************"

    os.system('clear')

    print(star_line)
    print(stars, "BATTLEBOATS!", stars)
    print(star_line)


def score():
    print("Use Arrow Keys for navigation")
    print("Use Space Key for Action  \n")
    print("Scope: +")
    print("Water: ~")
    print("Miss:  O")
    print("Hit:   X  \n")
    print("Turn: ", turns, "/", difficulty)
    print("hit boats: ", hit_boats)
    print("hit or miss: ", hit_miss, "\n")


def main_menu():

    option = [
        "Easy Mode",
        "Hard Mode",
        "Rule Book",
        "Exit Game"]

    choice = 0

    while(True):

        os.system('clear')

        logo()

        print("Use Arrow keys to navigate \nPress Enter to start a game\n")


def draw_graphics():

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

    if turns != 20:
        graphic_ocean[cursor_x, cursor_y] = "+"

    os.system('clear')

    for y in range(5):
        for x in range(5):
            print(graphic_ocean[x, y], end=" ")
        print("")

    print(hit_miss)


def spawn_boats():

    for boats in range(5):
        boat_x, boat_y = randint(0, 4), randint(0, 4), 

        while hidden_ocean[boat_x][boat_y] == 1:
            boat_x, boat_y = randint(0, 4), randint(0, 4)
        hidden_ocean[boat_x][boat_y] = 1


draw_graphics()
spawn_boats()

while (turns < 20):

    # Controls section
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
        turns += 1

        # What the numbers mean in hidden_ocean
        # Hidden Water = 0
        # Hidden Boat = 1
        # Shot boat = 2
        # Shot water = 3

        if hidden_ocean[cursor_x, cursor_y] == 0:
            hidden_ocean[cursor_x, cursor_y] = 3
            graphic_ocean[cursor_x, cursor_y] = "O"
            hit_miss = "you Missed !!"
            
        elif hidden_ocean[cursor_x, cursor_y] == 1:
            hidden_ocean[cursor_x, cursor_y] = 2
            graphic_ocean[cursor_x, cursor_y] = "X"
            hit_miss = "you hit a boat!"

    draw_graphics()
    hit_miss = ""
    