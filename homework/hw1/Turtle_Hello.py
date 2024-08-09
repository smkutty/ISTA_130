''' 
Author: Dan Charbonneau
Date: 1/17/2022
Class: ISTA 130
Section Leader: NA

Description:
This program will use a turtle from the turtle module to write 'HELLO'
'''

# put all of your import statements below this line and then delete this comment
import turtle

# put all of your function definitions below this line and then delete this comment

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

    # Move turtle to left to ensure HELLO is visible
    tallulah.penup()
    tallulah.back(300)
    tallulah.pendown()

    # write H
    tallulah.right(90)
    tallulah.forward(100)
    tallulah.back(50)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.back(100)
    tallulah.right(90)
    tallulah.penup()
    tallulah.forward(100)
    tallulah.pendown()
    
    # write E
    tallulah.back(50)
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.back(50)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.penup()
    tallulah.forward(50)
    tallulah.pendown()
    
    # write L
    tallulah.left(90)
    tallulah.forward(50)
    tallulah.back(100)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.penup()
    tallulah.forward(50)
    tallulah.pendown()

    # write second L
    tallulah.forward(50)
    tallulah.back(50)
    tallulah.left(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.penup()
    tallulah.forward(100)
    tallulah.pendown()
    
    # write O
    tallulah.forward(50)
    tallulah.right(90)
    tallulah.forward(100)
    tallulah.right(90)
    tallulah.forward(50)
    tallulah.right(90)
    tallulah.forward(100)

    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
