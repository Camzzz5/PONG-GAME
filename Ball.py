from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_creation()
        
    def ball_creation(self):
        self.shape("circle")
        self.color("white")
        self.pu()
        
    def ball_movement(self):
        self.goto(self.xcor()+10, self.ycor()+10)
            
    
        
        