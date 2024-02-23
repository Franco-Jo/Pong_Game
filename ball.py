from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.color('white')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.x_move = 13
        self.y_move = 10
        self.move_speed = 0.02

    def move(self):
        ycor = self.ycor() + self.y_move
        xcor = self.xcor() + self.x_move

        self.goto(xcor, ycor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.x_move = 13
        self.y_move = 10
        self.move_speed = 0.02
        self.bounce_x()






