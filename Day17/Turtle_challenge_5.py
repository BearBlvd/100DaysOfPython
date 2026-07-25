import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
tim.speed(10000)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return(r,g,b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading()+size_of_gap)
        tim.circle(100)

draw_spirograph(5)
screen=t.Screen()
screen.exitonclick()