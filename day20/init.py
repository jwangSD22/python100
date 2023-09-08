from turtle import Turtle

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(1,1)
        self.color('white')
        self.val = (0,0)
        self.next = None
        self.speed(2)
            


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(1,1)
        self.color('red')
        self.speed(0)
        self.penup()




