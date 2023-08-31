from turtle import Turtle

class GUI(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.speed(1)
        self.pensize(3)
        self.hideturtle()
        
    def initialize_net(self):
        self.setpos(0,-320)
        self.setheading(90)
        for _ in range(32):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
        
        
    
    def game_over(self):
        pass
    
        
