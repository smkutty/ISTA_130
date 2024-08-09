'''
Author: Sreelakshmi Kutty  
Date: 29 August 2023
Class: ISTA 130
Section Leader: <your section leader>

Description:
This program draws a square using Turtle
'''

# put all of your import statements below this line and then delete this comment
import turtle

# put all of your function definitions below this line and then delete this comment


#==========================================================
def main():
    '''
    Construct turtle and use it to draw a square
    '''
    # put main code here, make sure each line is indented one level, and delete this comment

    meena = turtle.Turtle()
    meena.pencolor("teal")
    meena.pensize(10)

    for x in range(4):
        meena.forward(90)
        meena.left(90)
    
    meena.penup()
    meena.forward(10)
    meena.pendown()
    meena.pencolor("red")

    for x in range(4):
        meena.forward(50)
        meena.left(90)


    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
