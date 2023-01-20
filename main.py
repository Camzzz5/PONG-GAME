from turtle import Turtle, Screen

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("pong")


POSITIONS = [(350,0),(350,20), (350,40), (350,-20), (350,-40)]
segments = []
for position in POSITIONS:
    segment = Turtle("square")
    segment.color("white")
    segment.pu()
    segment.goto(position)
    
    
    

screen.exitonclick()