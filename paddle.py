from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.paddlecreation()
        
        

    def paddlecreation(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid = 5)
        self.pu()
        self.goto(self.position)
        
    def go_up(self):
        self.goto(self.xcor(),self.ycor() +20)
   
    def go_down(self):
        self.goto(self.xcor(),self.ycor() -20)
            