# This program is a simple village sim.

from classes import *

def verify_coordinate(coordinate, axis):
    if axis == 'row':
        return coordinate in range(1, Village.ROWS + 1)
    if axis == 'col':
        return coordinate in range(1, Village.COLUMNS + 1)


def get_coordinates(structure):
    row = int(input("Please enter the row you would like to place the " + structure))
    if not verify_coordinate(row, 'row'):
        print("Invalid input, please try again.")
        return
    
    col = int(input("Please enter the column you would like to place the " + structure))
    if not verify_coordinate(col, 'col'):
        print("Invalid input, please try again.")
        return
    
    return (row, col)

def build_structure():
    pass

def plant_seed():
    pass

def shop():
    pass

def demolish():
    pass

def end_turn():
    pass

def main_input():
    message = """ 
    What would you like to do?
    (B)uild a structure, (P)lant a seed, (S)hop, (D)emolish a plot, or (E)nd turn?
    (both lowercase and uppercase letters are fine)"""

    valid_choices = ['B', 'P', 'S', 'D', 'E']

    choice = input(message).upper()

    if choice not in valid_choices:
        print("Invalid input, please try again.")
        return
    
    if choice == 'B':
        build_structure()
    elif choice == 'P':
        plant_seed()
    elif choice == 'S':
        shop()
    elif choice == 'D':
        demolish()
    elif choice == 'E':
        end_turn()
