from turtle import *
speed('fastest')
color('cyan')
bgcolor('black')
b = 200
screensize(600,600)
goto(280,70)
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1

exitonclick()