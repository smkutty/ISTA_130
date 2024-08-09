'''
Author: Sarah Stueve
Date: today
Class: ISTA 130
Section Leader: I'm the (wo)man

Description:
The program draws the name "COCA-COLA". 
Credit for the development of this script goes to Rich Thompson.
'''

# all import statements here, for example:
import turtle  # this is only needed if you're using turtle graphics

# all function definitions here, we'll define functions soon


#==========================================================
def main():
    '''
    Construct a turtle and use it write 'COCO-COLA'.
    '''
    # your code goes here, make sure it's indented one level
    
    # prepare the turtle - set its state and initial position
    tallulah = turtle.Turtle()
    turtle.bgcolor('black') # a function in the turtle module
    tallulah.pencolor('red')
    tallulah.pensize(10)
    tallulah.shape('turtle')
    tallulah.penup()
    tallulah.backward(200)
    tallulah.pendown()
    
    # draw a C
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.penup()
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.left(90)
    
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.pencolor('green')
    
    # draw an O
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.left(90)
    
    tallulah.penup()
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.pencolor('blue')
  
    # draw a C
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.penup()
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.left(90)
    
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.pencolor('gold')
    
    # draw an A
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.backward(12.5)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.right(180)
    
    tallulah.pencolor('magenta')
    
    # draw a hyphen
    tallulah.penup()
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.penup()
    tallulah.forward(12.5)
    tallulah.left(90)
    
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.pencolor('purple')

    # draw a C
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.penup()
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.left(90)
    
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.pencolor('darkgoldenrod')
    
    # draw an O
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.left(90)
    
    tallulah.penup()
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.pencolor('darkred')
    
    # draw an L
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.right(90)
    tallulah.forward(25)
   
    tallulah.penup()
    tallulah.forward(20)
    tallulah.pendown()
    tallulah.pencolor('darkgreen')
    
    # draw an A
    tallulah.left(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.backward(12.5)
    tallulah.right(90)
    tallulah.forward(25)
    tallulah.backward(25)
    tallulah.right(180)
    
    tallulah.hideturtle()
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
