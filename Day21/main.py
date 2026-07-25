import time
from turtle import Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#setting up player & movement
player = Player()
player.starting_line()
screen.listen()
screen.onkey(player.move_up,"Up")
#setting up car
car_manager=Car_Manager()
#setting up score bored
scoreboard=Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    #detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.incease_level()
        scoreboard.update_scoreboard()
    
    

screen.exitonclick()