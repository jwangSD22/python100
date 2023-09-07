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
        self.state = 'free'
        self.x_move = speedfactor
        self.y_move = speedfactor
        
    def move_ball(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x, new_y)
        
            # self.setheading(self.direction)
            # self.forward(self.sf)        
            screen.update()

            
    def bounce_x(self):
        self.x_move*=-1
        

    def bounce_y(self):
        self.y_move*=-1

    def ball_reset(self):
        self.goto(0,0)
        self.bounce_x()
        self.move_ball()
