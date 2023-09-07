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
        self.p1 = Paddle(-600,3)
        self.p2 = Paddle(600,3)
        self.ball = Ball(15)
        
    def start_game(self):
        while True:
            time.sleep(0.05)
            self.ball.move_ball()
            self.check_collision()
            
            # if the ball coordinate is in the same x-coordinate of where a paddle lies
            # need to cycle thru the paddle blocks of the paddle to see if there's a collision with any paddle
            
    
    def check_collision(self):
        temp = []
        closest = None
        p1_paddle_pos = self.p1.h[0][1].pos()
        p2_paddle_pos = self.p2.h[0][1].pos()

        ball_pos = self.ball.pos()
        
        if self.ball.ycor() > 300 or self.ball.ycor() < -300:
            self.ball.bounce_y()
            
        if self.ball.xcor()<=-620 or self.ball.xcor()>=620:
            
            coord = self.ball.xcor()
            
            if coord <=-620:
                self.scoreboard.player_2_score+=1
                self.scoreboard.publish_score()
            if coord >=620:
                self.scoreboard.player_1_score+=1
                self.scoreboard.publish_score()
            
            
            time.sleep(1)
            self.ball.ball_reset()
        
        
        if self.ball.xcor()==-600 and abs(p1_paddle_pos[1]-ball_pos[1])<60:
            # for block in self.p1.h:
            #     temp.append((self.ball.distance(self.p1.h[block][1]),self.p1.h[block][1]))
            # closest = min(temp,key=lambda x:x[0])
            # identity = closest[1].identifier

            self.ball.bounce_x()
        
        if self.ball.xcor()==600 and abs(p2_paddle_pos[1]-ball_pos[1])<60:
        # for block in self.p1.h:
        #     temp.append((self.ball.distance(self.p1.h[block][1]),self.p1.h[block][1]))
        # closest = min(temp,key=lambda x:x[0])
        # identity = closest[1].identifier

            self.ball.bounce_x()



g = Pong()
g.gui.initialize_net()
g.scoreboard.publish_score()
g.p1.initialize_player1()
g.p1.display()
g.p2.initialize_player2()
g.p2.display()

g.start_game()









screen.update()
screen.exitonclick()
