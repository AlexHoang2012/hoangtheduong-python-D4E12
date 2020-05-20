#Turtle 1

from turtle import *
shape("turtle")

for i in range(3, 8):
    for a in range(i):
        if i == 3:
            color("red")
        elif i == 4:
            color("blue")
        elif i == 5:
            color("brown")
        elif i == 6:
            color("yellow")
        else:
            color("grey")
        forward(100)
        left(360/i)
mainloop()

#Turtle 2
shape("square")


for i in range(1,6):
    begin_fill()
    for n in range(4):
        forward(100)
        left(90)
    forward(100)
    if i == 1:
        color("red")
    elif i == 2:
            color("blue")
    elif i == 3:
            color("brown")
    elif i == 4:
            color("yellow")
    else:
            color("grey")
    end_fill()
    
mainloop()

