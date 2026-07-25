from turtle import *

turtle=Turtle()
screen=Screen()

for _ in range(15):
    turtle.forward(5)
    turtle.penup()
    turtle.forward(5)
    turtle.pendown()

screen.exitonclick()