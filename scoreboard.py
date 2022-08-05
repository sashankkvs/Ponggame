from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
    def updated_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font = ("Courrier", 40, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courrier", 40, "normal"))
    def l_point(self):
        self.l_score+=1
        self.updated_score()
    def r_point(self):
        self.r_score += 1
        self.updated_score()
    def player_win(self):
        self.goto(0,0)
        if self.l_score == 3:
            self.write(f"The left player has won", align="center", font = ("Arial", 20, "normal"))
        elif self.r_score == 3:
            self.write(f"The right player has won", align="center", font=("Arial", 20, "normal"))
        