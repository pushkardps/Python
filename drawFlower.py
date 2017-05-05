# program to draw a flower

import turtle # import turtle package to enable drawing

def draw_flower():
    abe = turtle.Turtle()
    abe.shape("turtle")
    abe.color("blue")
    abe.speed(30)

    i=0
    while i < (360/7.5):
        abe.right(7.5)
        i = i + 1
        m=0
        while m < 2:
            abe.right(30)
            abe.forward(100)
            abe.right(150)
            abe.forward(100)
            m = m + 1
        
    abe.right(90)
    abe.forward(180)            

window = turtle.Screen()
window.bgcolor("white")
draw_flower()
window.exitonclick()
