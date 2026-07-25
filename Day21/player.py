from turtle import Turtle;
STARTING_POSITION = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    #Creating(INSTANCIATING) My Player Object
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        
    #MOVING Forwad 
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    #go to start  
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    #Resting Player Position @ Finish Line
    def starting_line(self):
        if(self.ycor()>=FINISH_LINE_Y):
            self.goto(STARTING_POSITION)

    #detect successful crossing
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

    






