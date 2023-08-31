from turtle import Turtle, Screen

screen = Screen()

class Ball(Turtle):
    def __init__(self,speedfactor=10):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.speed(0)
        self.direction = 180
        self.sf = speedfactor
        self.state = 'free'
        
    def move_ball(self):
        if self.state == 'free':
            self.setheading(self.direction)
            self.forward(self.sf)        
            screen.update()
