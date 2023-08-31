from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.speed(0)
        self.hideturtle()
        
        self.player_1_score = 0
        self.player_2_score = 0
        

    def publish_score(self):
        self.setpos(-320,220)
        self.write(f'{self.player_1_score}',align='center',font=('Courier',60))
        self.setpos(320,220)
        self.write(f'{self.player_2_score}',align='center',font=('Courier',60))

        
