#!/usr/bin/env python3

import turtle
turt  = turtle.Turtle() #Create the turtle
win = turtle.Screen() #create window for the turtle
turt.shape("square") #set Turtle shape and size
turt.turtlesize(0.5)

#Different possible Key inputs
def upArrow():
    turt.setheading(90) #turns to the correct direction
    turt.forward(2) #moves set amount

def downArrow():
    turt.setheading(270)
    turt.forward(2)

def rightArrow():
    turt.setheading(0)
    turt.forward(2)

def leftArrow():
    turt.setheading(180)
    turt.forward(2)

def quit():
    win.bye()

#listens for the different possible keys and calls the correct method
win.onkey(upArrow, "w")
win.onkey(downArrow, "s")
win.onkey(rightArrow, "d")
win.onkey(leftArrow, "a")
win.onkey(quit, "q")
win.listen()

turtle.mainloop()