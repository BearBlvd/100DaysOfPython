from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def forward():
    tim.forward(10)

def backwards():
    tim.backward(10) 

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=forward,key='W')
screen.onkey(fun=backwards,key='S')
screen.onkey(fun=turn_right,key='A')
screen.onkey(fun=turn_left,key='D')
screen.onkey(fun=clear,key='C')
screen.exitonclick()