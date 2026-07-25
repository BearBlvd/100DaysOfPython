import turtle as t
import random

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)

tim=t.Turtle()
t.colormode(255)
tim.speed("Fastest")
screen=t.Screen()
tim.circle(100)

screen.exitonclick()