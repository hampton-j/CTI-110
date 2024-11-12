# CTI 110
# P4LAB1 - Turtles
# hamptonj
# draw Shapes and snowflakes using for loops

#Set up the turtle

import turtle
t = turtle.Turtle()

#add some display options
t.pensize(6)
t.pencolor("plum4")
t.shape ("turtle")
for side in range(20):
    t.forward(200)
    t.right (45)
    t.forward (50)
    t.right (180)
    # add a pokey bit
    t.left(90)
    t.forward(20)
    t.back(20)
    t.right(90)
    # end pokey bit
    t.forward (50)
    
    



