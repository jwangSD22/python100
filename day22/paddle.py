from turtle import Turtle, Screen

screen = Screen()


    


class PaddleBlock(Turtle):
    def __init__(self,identifier):
        super().__init__()
        self.penup()
        self.color('white')
        self.speed(0)
        self.shape('square')
        self.identifier = identifier
        

class Paddle():
    def __init__(self,xcoord,speed):
        self.h = {
            -2 : (40,PaddleBlock('u2')),
            -1 : (20,PaddleBlock('u1')),
            0 : (0, PaddleBlock('c')),
            1 : (-20, PaddleBlock('b1')),
            2 : (-40, PaddleBlock('b2'))
        }
        self.xcoord = xcoord
        self.ycoord = 0
        self.cpu = False
        self.paddle_speed = speed
        if speed == 1:
            self.paddle_speed = 10
        elif speed == 2:
            self.paddle_speed = 20
        elif speed == 3:
            self.paddle_speed = 30
            
        
    def initialize_player1(self):
            screen.onkeypress(self.move_up,'w')
            screen.onkeypress(self.move_down,'s')

    def initialize_player2(self):
            screen.onkeypress(self.move_up,'Up')
            screen.onkeypress(self.move_down,'Down')

    def move_up(self):
        self.h[0][1].setheading(90)
        paddle_top_y = self.h[-2][1].pos()[1]
        if paddle_top_y >= 320:
            return
        self.h[0][1].forward(self.paddle_speed)
        self.ycoord = self.h[0][1].pos()[1]
        self.display()
        screen.update()
        
    def move_down(self):
        self.h[0][1].setheading(270)
        paddle_top_y = self.h[2][1].pos()[1]
        if paddle_top_y <= -320:
            return
        self.h[0][1].forward(self.paddle_speed)
        self.ycoord = self.h[0][1].pos()[1]
        self.display()
        screen.update()
        
    
    def display(self):
        # x is fixed for paddle
        for block in self.h:
            yfactor = self.h[block][0]
            self.h[block][1].setpos(self.xcoord,self.ycoord+yfactor)
            


        
    

