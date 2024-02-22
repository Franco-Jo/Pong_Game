from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=10, stretch_len=2)
        self.color('white')
        self.pu()
        self.goto(position)

    def move_up(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def move_down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)
