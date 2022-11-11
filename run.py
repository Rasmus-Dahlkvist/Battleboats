# Write your code to expect a terminal of 80 characters wide and 24 rows high
# import os
# from random import randint
import numpy as np
# from getkey import getkey, keys

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

    for y in range(5):
        for x in range(5):
            print(graphic_ocean[x, y], end=" ")
        print("")


draw_graphics()

