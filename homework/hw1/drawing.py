'''
Author: Sreelakshmi Kutty
Date: 7 September 2023
Class: ISTA 130
Section Leader: Huy Tran

Description:
Homework 1 Problem 3> Player's Choice
Draw an outrageous picture using turtle
'''

# put all of your import statements below this line and then delete this comment
import random
import turtle

# put all of your function definitions below this line and then delete this comment
def red_flower(me, x, y):
    '''
    This function draws a red flower at given point

    Parameters---
    me: a turtle that is used to draw
    x: an int to determine x coordinate
    y: an int to determine y coordinate

    Returns: None
    '''
    #Draw 4 petals
    jump(me, x, y)
    me.pencolor('red')
    for i in range(0,4):
        me.circle(30, 180)
        me.left(90)
    
    #Draw stem
    me.pencolor('darkgreen')
    jump(me, x+30, y+30)
    me.right(90)
    me.forward(100)

    me.left(90) #faces back to left
    return None

def yellow_flower(me, x, y):
    '''
    This function draws a yellow flower with stem at specified location

    Parameters---
    me: a turtle that is used to draw
    x: an int to determine x coordinate
    y: an int to determine y coordinate

    Returns: None
    '''
    #Draw stem
    jump(me, x, y)
    me.pencolor('darkgreen')
    me.right(90)
    me.forward(150)

    #Draw 12 petals
    me.pencolor('goldenrod')
    me.pensize(20)
    jump(me, x, y)
    for i in range (0, 12):
        me.forward(40)
        me.back(40)
        me.left(30)
    jump(me, x, y)

    #Readjust and turn back left
    me.pensize(10)
    me.left(90) 


def draw_grass(me, x, y):
    '''
    This function raws a line of grass starting from specified coordinate

    Parameters---
    me: a turtle that is used to draw
    x: an int to determine x coordinate
    y: an int to determine y coordinate

    Returns: None
    '''
    jump(me, x, y)
    me.pencolor('lightgreen')
    me.left(90)
    hold = x #takes x coord and updates in loop
    for i in range(0, 55):
        me.forward(10)
        hold += 10
        jump(me, hold, y)
    me.right(90) #faces back to left

def rainbow(me, x, y):
    '''
    This function draws a rainbow at sepcified location

    Parameters---
    me: a turtle that is used to draw
    x: an int to determine x coordinate
    y: an int to determine y coordinate

    Returns: None
    '''
    #change turtle properties and draw red arch
    me.pensize(15)
    jump(me, x, y)
    me.pencolor('red')
    me.circle(100, 180)

    #draw yellow arch
    jump(me, x-10, y)
    me.left(180)
    me.pencolor('yellow')
    me.circle(90, 180)

    #draw green arch
    jump(me, x-20, y)
    me.left(180)
    me.pencolor('lightgreen')
    me.circle(80, 180)

    #draw blue arch
    jump(me, x-30, y)
    me.left(180)
    me.pencolor('blue')
    me.circle(70, 180)

    #draw purple arch
    jump(me, x-40, y)
    me.left(180)
    me.pencolor('purple')
    me.circle(60, 180)

    #readjust and face back left
    me.pensize(10)
    me.left(90)

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
    This file draws a colorful picture of flowers and rainbows
    '''

    # Instantiate turtle object
    meena = turtle.Turtle()

    # Change turtle properties
    meena.speed(0)
    meena.pensize(10)
    meena.shape('turtle')

    # Draw 3 yellow flowers
    yellow_flower(meena, 0, -125)
    yellow_flower(meena, -150, -125)
    yellow_flower(meena, 150, -125)

    # Draw 1 rainbow
    meena.left(90)
    rainbow(meena, 150, 150)

    # Draw 5 red flowers
    x_red = -250 #placeholder x coordinate for red flowers

    for i in range (0, 5):
        red_flower(meena, x_red, -200)
        x_red += 100

    # Draw 3 lines of grass
    draw_grass(meena, -275, -275)
    draw_grass(meena, -285, -290)
    draw_grass(meena, -275, -305)

    # Draw 10 more rainbows because why not
    for i in range(0, 10):
        meena.left(90)
        x_random = random.randint(-250, 300)
        y_random = random.randint(0, 100)
        rainbow(meena, x_random, y_random)
    

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
