from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
#setting up screen
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
#Setting Up Paddle & Ball
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()
#Setting up Action Keys
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
#creating game loop
game_is_on=True
while game_is_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()
    #detecting collision with wall
    if ball.ycor()>280 or ball.ycor()<-280 :
        #needs to bounce
        ball.bounce_wall()
    #detecting collision with r_paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_paddle()
    # detect if right pedal misses
    if ball.xcor()>380:
        ball.reset_position()
        score.l_point()
    #detect if left pedal misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()