from turtle import *
import random

turtle=Turtle()
screen=Screen()

sides=3
colors=["lime green","dark orange","magenta","dark red","dodger blue"]
while(sides<=10):

    for _ in range(sides):
        turtle.forward(100)
        turtle.right(360/sides)
        
    turtle.color(random.choice(colors))
    sides+=1



screen.exitonclick()