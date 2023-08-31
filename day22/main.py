from turtle import Screen
from gui import GUI
from score import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=1280, height = 640)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)
screen.listen()

class Pong:
    def __init__(self):
        self.gui = GUI()
        self.scoreboard = Scoreboard()
        # arg1 defines x-coordinate of paddle
        # arg2 defines paddle speed (1,2,3)
        self.p1 = Paddle(-600,1)
        self.p2 = Paddle(600,3)
        self.ball = Ball(10)






g = Pong()
g.gui.initialize_net()
g.scoreboard.publish_score()
g.p1.initialize_player1()
g.p1.display()
g.p2.initialize_player2()
g.p2.display()










screen.update()
screen.exitonclick()
