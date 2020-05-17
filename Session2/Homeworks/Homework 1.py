
from turtle import *

#Không vẽ được hình đầu tiên

shape("turtle")
speed(-1)
n = int(input ("mời nhậP số cạnh: "))
for i in range(3, n+1):
    
    for a in range(i):

        if(i%2==0):
            color("red")
        else:
            color("blue")

        forward(100)
        left(360/i)

mainloop()