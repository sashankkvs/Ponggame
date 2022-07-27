from turtle import Turtle, Screen
from paddle import Paddle
from pongball import Pongball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_Paddle = Paddle((350,0))
l_Paddle = Paddle((-350, 0))

pongball = Pongball()
scoreboard = Scoreboard()
screen.listen()


screen.onkeypress(key = "Up", fun = r_Paddle.move_up)
screen.onkeypress(key = "Down", fun =  r_Paddle.move_down)
screen.onkeypress(l_Paddle.move_up, "w")
screen.onkeypress(l_Paddle.move_down, "s")

game_play = True
while game_play:
    time.sleep(pongball.move_speed)
    screen.update()
    pongball.move_ball()
    if pongball.ycor() > 280 or pongball.ycor() < -280:
        pongball.bounce_bally()

    elif r_Paddle.distance(pongball)<40 and r_Paddle.xcor()>330 or l_Paddle.distance(pongball)<40 and l_Paddle.xcor()<-330:
        pongball.bounce_ballx()

    elif pongball.xcor() > 380:
        pongball.reset_ball()
        scoreboard.l_point()
    elif pongball.xcor() < -380:
        pongball.reset_ball()
        scoreboard.r_point()
    if scoreboard.l_score == 10:
        scoreboard.goto(0, 0)
        scoreboard.write(f"The left player has won", align="center", font=("Arial", 20, "normal"))
        game_play = False
    elif scoreboard.r_score == 10:
        scoreboard.goto(0, 0)
        scoreboard.write(f"The right player has won", align="center", font=("Arial", 20, "normal"))
        game_play = False













print(screen.exitonclick())
