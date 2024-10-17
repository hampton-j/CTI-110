# CTI 110
# P2LAB2B - Turtle
#Hampton
#10/17/24

# using lists and loops to draw

import turtle
t = turtle.Turtle()
# remember pensize , pencolor
t. pensize(8)
t.pencolor("blue")

# simple loop
for length in [100, 50, 100, 200]:
    t.forward(length)
    t.right(90)
    t.left(90)

    t.pencolor("aquamarine3")
    for length in [10,20,60,70,40,45,50,30,35,45]:
        t.forward(length)
        t.right(90)


sides = 5
length = 100
angle = 360 / sides

for color in ["pink", "lightskyblue3", "Lightskyblue1", "azure3", "mediumpurple3"]:
    t.pencolor (color)
    t.forward (length)
    t.right(angle)


