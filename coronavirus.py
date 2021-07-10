from turtle import *
color("red")
bgcolor("grey")
speed(15)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b += 1

done()