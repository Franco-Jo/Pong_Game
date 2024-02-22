from turtle import Turtle
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=2120, height=1100)
screen.bgcolor('black')
screen.title('PONG')
screen.listen()
screen.tracer(0)

r_paddle = Paddle((1000, 0))
l_paddle = Paddle((-1000, 0))

screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
