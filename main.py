from turtle import Turtle, Screen
import time
from paddle import Paddle
from Ball import Ball

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()

screen.listen()  
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down") 
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down,"s") 
 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.ball_movement()

screen.exitonclick()