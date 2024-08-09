'''
Author: Sreelakshmi Kutty
Date: 6 Septmeber 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 1 Problem 1> Name
Draw your name using functions
'''

# import statements
from re import M
import turtle

# functions for drawing letters
def draw_s(my_turtle):
    '''
    This function draws letter S

    Parameters---
    me: a turtle that is used to draw

    Returns: None
    '''
    my_turtle.forward(100)
    my_turtle.left(90)
    my_turtle.forward(80)
    my_turtle.left(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(80)
    my_turtle.right(90)
    my_turtle.forward(100)
    return None

def draw_r(my_turtle):
    '''
    This function draws letter R

    Parameters---
    me: a turtle that is used to draw

    Returns: None
    '''
    my_turtle.forward(160)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(80)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.left(140)
    my_turtle.forward(125)
    my_turtle.left(40)
    return None

def draw_e(my_turtle):
    '''
    This function draws letter E

    Parameters---
    me: a turtle that is used to draw

    Returns: None
    '''
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(80)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.back(100)
    my_turtle.left(90)
    my_turtle.forward(80)
    my_turtle.right(90)
    my_turtle.forward(100)
    return None

#==========================================================
def main():
    '''
    Program will write "SREE" using turtle and functions above
    '''
    # instantiate turtle
    meena = turtle.Turtle()

    # change turtle properties
    meena.speed(0)
    meena.pencolor('red')
    meena.pensize(10)
    meena.shape('turtle')

    # position turtle to left
    meena.penup()
    meena.back(300)
    meena.pendown()

    # write S and reposition
    draw_s(meena)
    meena.penup()
    meena.forward(50)
    meena.right(90)
    meena.forward(160)
    meena.left(180)
    meena.pendown()

    # write R and reposition
    draw_r(meena)
    meena.penup()
    meena.forward(150)
    meena.left(180)
    meena.pendown()

    # write E and reposition
    draw_e(meena)
    meena.penup()
    meena.forward(150)
    meena.right(90)
    meena.forward(160)
    meena.right(90)
    meena.pendown()

    # write second E
    draw_e(meena)

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
