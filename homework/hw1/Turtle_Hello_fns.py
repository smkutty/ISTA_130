''' 
Author: Dan Charbonneau
Date: 1/17/2022
Class: ISTA 130
Section Leader: NA

Description:
This program will use a turtle from the turtle module to write 'HELLO' using functions
'''

# put all of your import statements below this line and then delete this comment
import turtle

# put all of your function definitions below this line and then delete this comment
def write_H(a_turtle):
    '''
    This function draws an H and places cursor/turtle in the upper left corner of next letter, facing right, with 50px space between letters
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.back(50)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.back(100)
    a_turtle.right(90)
    a_turtle.penup()
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.pendown()

def write_E(a_turtle):
    '''
    This function draws an E and places cursor/turtle in the upper left corner of next letter, facing right, with 50px space between letters
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.forward(50)
    a_turtle.back(50)
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.back(50)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.right(90)
    a_turtle.forward(50)
    a_turtle.penup()
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.right(90)
    a_turtle.pendown()

def write_L(a_turtle):
    '''
    This function draws an L and places cursor/turtle in the upper left corner of next letter, facing right, with 50px space between letters
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.penup()
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.pendown()

def write_O(a_turtle):
    '''
    This function draws an O and places cursor/turtle in the upper left corner of next letter, facing right, with 50px space between letters
    Parameters:
        :a_turtle: turtle object
    Returns:
        None
    '''
    a_turtle.forward(50)
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.right(90)
    a_turtle.forward(50)
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.penup()
    a_turtle.right(90)
    a_turtle.forward(100)
    a_turtle.pendown()
#==========================================================
def main():
    '''
    Writes the word 'HELLO' using a turtle
    '''
    #Set screen size
    
    
    # Initiate turtle
    tallulah = turtle.Turtle()

    # Change turtle properties
    tallulah.shape('turtle')
    tallulah.pensize(10)
    tallulah.pencolor('blue')

    # Move turtle to left
    tallulah.penup()
    tallulah.back(300)
    tallulah.pendown()

    # write H
    write_H(tallulah)
    
    # write E
    write_E(tallulah)

    # write L
    write_L(tallulah)

    # write L
    write_L(tallulah)
    
    # write O
    write_O(tallulah)

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
