from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_creation()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def ball_creation(self):
        self.shape("circle")
        self.color("white")
        self.pu()
        
    def ball_movement(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)
        
    def bounce_y(self):
        self.y_move *=-1
        
    def bounce_x(self):
        self.x_move *=-1
        
    def restart(self):
        self.x_move *=-1
        self.goto(0, 0)
        self.ball_movement()
        self.move_speed = 0.1
                
    
        
        