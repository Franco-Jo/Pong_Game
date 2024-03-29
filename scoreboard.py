from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """create and update scoreboard"""
        self.clear()
        self.goto(-200, 375)
        self.write(self.l_score, align='center', font=("Terminal", 80, "normal"))
        self.goto(200, 375)
        self.write(self.r_score, align='center', font=("Terminal", 80, "normal"))

    def l_point(self):
        """add score to left player and update"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """add score to right player and update"""
        self.r_score += 1
        self.update_scoreboard()
