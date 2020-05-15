from turtle import *

shape("turtle")
speed(-1)
n = int(input ("mời nhậP số cạnh: "))
for i in range(3, n+1):
    for a in range(i):
        forward(100)
        left(360/i)

mainloop()