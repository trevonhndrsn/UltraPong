from turtle import Screen, Turtle
from paddle import Paddle
from Ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.title("ULTRA PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
Ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(Ball.move_speed)
    screen.update()
    Ball.move()

    if Ball.ycor() > 280 or Ball.ycor() < -280:
        Ball.bounce_y()

    if Ball.distance(r_paddle) < 50 and Ball.xcor() > 320 or Ball.distance(l_paddle) < 50 and Ball.xcor() < -320:
        Ball.bounce_x()

    if Ball.xcor() > 380:
        Ball.reset_position()
        scoreboard.l_point()

    if Ball.xcor() < -380:
        Ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()