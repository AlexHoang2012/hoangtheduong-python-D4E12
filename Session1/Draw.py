from turtle import *

shape("turtle")
speed(-1)
color('green')
n=input("Xin mời nhập số: ")

for i in range (int(n)):
    forward(100)
    left(360/int(n))


mainloop()
