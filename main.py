from turtle import Turtle, Screen
import time

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_len=1, stretch_wid = 5)
paddle.pu()
paddle.goto(350,0)
       
def go_up():
    paddle.goto(paddle.xcor(),paddle.ycor() +20)
   
def go_down():
    paddle.goto(paddle.xcor(),paddle.ycor() -20)

screen.listen()  
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down") 
 
game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()