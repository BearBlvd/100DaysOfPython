import turtle as t
import random

turtle=t.Turtle()
screen=t.Screen()
moves=[0,90,180,270]
size=5
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

while(turtle.pensize()<=100):
    turtle.pencolor(random_color()) 
    turtle.pensize(size)
    turtle.speed(size)
    turtle.right(moves[random.randrange(0,4)])
    turtle.forward(20)
    turtle.setheading(random.choice(moves))
    size=+5
       

screen.exitonclick()