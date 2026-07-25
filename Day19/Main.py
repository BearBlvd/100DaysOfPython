from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time
  
#Screen setup
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#Snake setup
snake=Snake()
#Food setup 
food=Food()
#Score Board
scoreboard=Scoreboard()
#Snake motion
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.update_scoreboard()
    #detecting collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
        
    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.update_scoreboard()
        scoreboard.reset()
        snake.reset()
        game_is_on=False

    #detect collion with tail
    for segment in snake.segments:
        if segment ==  snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.update_scoreboard()
            scoreboard.reset()
            snake.reset()
            game_is_on=False
            

scoreboard.game_over(game_is_on)     
screen.exitonclick()