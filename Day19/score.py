from turtle import Turtle
ALIGNMENT = "Center"
FONT=("Courier",24,"normal")
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.game_over(game_is_on=True)
        self.goto(0,265)
        self.hideturtle()
        self.write(f"score :{self.score}",False,ALIGNMENT,FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"score :{self.score}",False,ALIGNMENT,FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"score :{self.score}| High Score: {self.high_score}",False,ALIGNMENT,FONT)


    def reset(self):
        if self.score>int(self.high_score):
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()

    def game_over(self,game_is_on):
        if game_is_on==False:
            #if game is on we write high score
            with open("data.txt",mode='w')as file_obj:
                self.high_score=file_obj.write(f"{self.high_score}")
        else :
            with open("data.txt",) as file_obj:
                self.high_score=str(file_obj.read())
    
    

   
        



    

