from turtle import Turtle

class Pongball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.x_new = 10
        self.y_new = 10
        self.move_speed = 0.1
    def move_ball(self):
        x_move = self.xcor() + self.x_new
        y_move = self.ycor() + self.y_new
        self.goto(x_move, y_move)
    def bounce_bally(self):
        self.y_new *= -1
    def bounce_ballx(self):
        self.x_new *= -1
        self.move_speed *= 0.9
    def reset_ball(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce_ballx()
    
        
        