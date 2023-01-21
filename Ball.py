from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_creation()
        self.x_move = 10
        self.y_move = 10
        
    def ball_creation(self):
        self.shape("circle")
        self.color("white")
        self.pu()
        
    def ball_movement(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
        
    def bounce(self):
        self.y_move *=-1
        
            
    
        
        