from turtle import Turtle, Screen
import time
from paddle import Paddle
from Ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()  
screen.onkey(paddle_r.go_up,"Up")
screen.onkey(paddle_r.go_down,"Down") 
screen.onkey(paddle_l.go_up,"w")
screen.onkey(paddle_l.go_down,"s") 
 
game_is_on = True


while game_is_on:
 
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_movement()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
        
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()
        ball.move_speed*=0.9
       
        
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()
        
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()



screen.exitonclick()