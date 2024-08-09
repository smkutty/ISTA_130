'''
Name: Sreelakshmi Kutty
Date: 14 Septmember 2023
Class: ISTA 130
Section Leader: Huy Tran

Homework 3 > Functions and Loops
Write 8 Functions to practice functions
and loops
'''

# Import packages
from cgitb import text
import math, random

# My 8 functions

def print_word(num, str):
    '''
    This function prints out word a specified number of times

    Parameters---
    num: number of times to print (int)
    str: word to print out (string)

    Returns: None
    '''
    for i in range(num):
        print(i+1, '-->', str)
    return None

def bacteria(mins, gens):
    '''
    This function prints out bacterial population after
    specified number of generations and minutes

    Parameters---
    num: number of times to print (int)
    str: word to print out (string)

    Returns: None
    '''
    for i in range(gens):
        print('after', mins*(i+1), 'minutes: ', 2**(i+1), 'bacteria')
    return None

def convert_to_copper(gold, silver, copper):
    '''
    This function prints out total converted copper from
    given gold, silver, and coppier pieces

    Parameters---
    gold: total gold pieces (int)
    silver: total silver pieces (int)
    copper: total copper pieces (int)

    Returns: None
    '''
    total = (gold*50) + (silver*5) + copper
    print(gold, 'gp,', silver, 'sp,', copper, 'cp converted to copper is:', total, 'cp')
    return None

def convert_from_copper(total):
    '''
    This function prints out total gold, silver, and copper
    converted from given number of copper pieces

    Parameters---
    copper: total coppier pieces to convert (int)

    Returns: None
    '''
    gold = int(total / 50)
    silver = int((total%50) / 5)
    copper = total-((gold*50) + (silver*5))
    print(total, 'copper pieces is:', gold, 'gp,', silver, 'sp,', copper, 'cp')
    return None

def repeat_word(str, rows, cols):
    '''
    This function prints out word repeated in
    specified number of rows and columns

    Parameters---
    str: word to repeat (string)
    rows: number of rows (int)
    cols: number of columns (int)

    Returns: None
    '''
    for i in range(rows):
        print(str * cols)
    return None

def text_triangle(num):
    '''
    This function prints out a triangle with a 
    specified height

    Parameters---
    num: number of lines in triangle (int)

    Returns: None
    '''
    for i in range(num-1):
        print('X'*(i+1))
    print('X'*num)
    return None

def surface_area_of_cylinder(r, h):
    '''
    This function prints out the surface area of
    a cylinder with specified radius and height

    Parameters---
    r: radius (float)
    h: height (float)

    Returns: None
    '''
    area = (2*math.pi * (r**2)) + (2*math.pi * r *h)
    print('The surface area of a cylinder with radius', r, 'and height', h, 'is', area)
    return None

def tree_height(base, length):
    '''
    This function prints out the tree height based 
    on specified length of kite and distance to tree

    Parameters---
    base: distance to tree (float)
    length: length of kite string (float)

    Returns: None
    '''
    height = math.sqrt((length**2)-(base**2))
    print('Kite string:', length)
    print('Distance:', base)
    print('Height:', height)
    return None



def main():
    '''
    This file calls the above functions to test and troubleshoot
    '''

    #Testing my functions
    print('Testing print_word')
    print_word(3, 'banana')

    print('\n Testing bacteria')
    bacteria(10, 5)

    print('\n Test convert_to_copper')
    convert_to_copper(5, 10, 7)

    print('\n Test convert_from_copper')
    convert_from_copper(200)
    convert_from_copper(1107)
    convert_from_copper(3242)
    convert_from_copper(208)

    print('\n Test repeat_word')
    repeat_word('Goblin', 3, 5)

    print('\n Test text_triangle')
    text_triangle(3)
    text_triangle(0)

    print('\n Test surface_area_of_cylinder')
    surface_area_of_cylinder(10.0, 10.0)
    surface_area_of_cylinder(0.0, 1.0)

    print('\n Test tree_height')
    tree_height(300, 500)
    tree_height(100, 141.421356)

if __name__ == '__main__':
    main()
