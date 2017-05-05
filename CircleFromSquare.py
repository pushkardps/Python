# Program to draw shapes using turtle library package in python

import turtle # import turtle library to use turtle class to draw shapes

# define art function
def draw_art():
          
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(20)

    m=0
    while m < 75:
        brad.right(5)
        m = m+1
        i=0
        while i < 4 :
            brad.forward(100)
            brad.right(90)
            i=i+1
 


window = turtle.Screen() # create screen to draw shape
window.bgcolor("red")    # set background colour
draw_art()            # call square function
window.exitonclick()     # exit by clicking on screen




 

