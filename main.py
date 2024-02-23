from turtle import Turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=2120, height=1100)
screen.bgcolor('black')
screen.title('PONG')
screen.listen()
screen.tracer(0)

r_paddle = Paddle((1000, 0))
l_paddle = Paddle((-1000, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(0.02)
    screen.update()
    ball.move()

    # detect collision with top and bottom walls
    if ball.ycor() > 527 or ball.ycor() < - 527:
        ball.bounce_y()

    # not perfect, get dribble effect on the ends of paddle
    # detect collision with paddle
    if ball.distance(r_paddle) < 130 and ball.xcor() > 950 or ball.distance(l_paddle) < 130 and ball.xcor() < -950:
        ball.bounce_x()

    if ball.xcor() > 1250:
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.reset()

    if ball.xcor() < -1250:
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.reset()
screen.exitonclick()
