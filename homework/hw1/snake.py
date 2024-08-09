'''
Author: Sreelakshmi Kutty
Date: 6 September 2023
Class: ISTA 130
Section Leader: Huy Tran

Description: 
Homework 1 Problem 2> Snake
Draw a snake using polygons
'''

# import statements
import turtle

# functions for polygons and jump
def triangle(me, length):
    '''
    This function draws a triangle with given length

    Parameters---
    me: a turtle that is used to draw
    length: an int that determines the size of triangle

    Returns: None
    '''
    me.forward(length)
    me.left(120)
    me.forward(length)
    me.left(120)
    me.forward(length)
    me.left(120)
    return None

def square(me, length):
    '''
    This function draws a square with given length

    Parameters---
    me: a turtle that is used to draw
    length: an int that determines the size of square

    Returns: None
    '''
    me.forward(length)
    me.left(90)
    me.forward(length)
    me.left(90)
    me.forward(length)
    me.left(90)
    me.forward(length)
    me.left(90)
    return None

def pentagon(me, length):
    '''
    This function draws a pentagon with given length

    Parameters---
    me: a turtle that is used to draw
    length: an int that determines the side length of pentagon

    Returns: None
    '''
    me.forward(length)
    me.left(72)
    me.forward(length)
    me.left(72)
    me.forward(length)
    me.left(72)
    me.forward(length)
    me.left(72)
    me.forward(length)
    me.left(72)
    return None

def hexagon(me, length):
    '''
    This function draws a hexagon with given length

    Parameters---
    me: a turtle that is used to draw
    length: an int that determines the side length of hexagon

    Returns: None
    '''
    me.forward(length)
    me.left(60)
    me.forward(length)
    me.left(60)
    me.forward(length)
    me.left(60)
    me.forward(length)
    me.left(60)
    me.forward(length)
    me.left(60)
    me.forward(length)
    me.left(60)
    return None

def jump(me, x, y):
    '''
    This function makes turtle jump to specified location

    Parameters---
    me: a turtle that is used to draw
    x: an int to determine x coordinate
    y: an int to determine y coordinate

    Returns: None
    '''
    me.penup()
    me.goto(x,y)
    me.pendown()
    return None



#==========================================================
def main():
    '''
    Calls polygon functions to draw a snake
    '''
    # instantiate turtle object
    meena = turtle.Turtle()

    # change turtle properties
    meena.speed(0)
    meena.pencolor('red')
    meena.pensize(10)
    meena.shape('turtle')

    # position turtle to left
    jump(meena, -250, 0)
    meena.left(90)

    # draw first triangle
    triangle(meena, 100)
    jump(meena, -150, 0)
    meena.pencolor('blue')

    # draw square
    square(meena, 100)
    jump(meena, 23, 0)
    meena.pencolor('orange')

    # draw two hexagons
    hexagon(meena, 100)
    jump(meena, 196, 0)
    meena.pencolor('goldenrod')
    hexagon(meena, 100)
    meena.left(252)
    meena.pencolor('black')

    # draw end pentagon
    pentagon(meena, 100)
    jump(meena, -150, 0)
    meena.pencolor('yellow')
    meena.left(48)

    # draw middle triangles
    triangle(meena, 100)
    meena.forward(100)
    meena.right(60)
    triangle(meena, 100)
    #meena.forward(100)
    jump(meena, 23, 0)
    meena.left(60)
    triangle(meena, 100)
    meena.forward(100)
    meena.right(60)
    triangle(meena, 100)

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
