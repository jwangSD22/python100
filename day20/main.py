from turtle import Screen, Turtle
from random import randint
from init import snake, food
import time


screen = Screen()
screen.setup(width=640, height = 640)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


speed = 2


def add_to_tail(snakehead):

    snake = Turtle()
    snake.penup()
    snake.speed(0)
    snake.shape('square')
    snake.color('white')
    snake.val = None
    snake.next = None
    snake.prev = None

    current = snakehead

    if snakehead.next == None:
        snakehead.next = snake
        snake.setpos(snakehead.prev)
    else:
        #iterate through snake to get to tail
        while current.next != None:
            current = current.next
        current.next = snake
        snake.setpos(current.prev)


def update_whole_snake(snakehead):
    head_coord = snakehead.pos()

    if snakehead.next == None:
        return True
    else:
        current = snakehead
        while current.next:
            current.next.prev = current.next.pos()
            if are_positions_equal(head_coord,current.next.pos()):
                return False
            current.next.setpos(current.prev)
            current = current.next
    return True

def are_positions_equal(pos1, pos2):
    return round(pos1[0], 2) == round(pos2[0], 2) and round(pos1[1], 2) == round(pos2[1], 2)



class SnakeGame:
    def __init__(self):
        self.snakehead = snake
        self.food = food
        self.food_xy = None
        self.turtle_pos_hash = {(0.00,0.00):True}
        self.tail = None
        self.coord = None
        self.score = 0

    def gen_food_loc(self):
        x = randint(-15,15)*20
        y = randint(-15,15)*20
        # if these values are okay, then proceed, else, regenerate
        self.food_xy = (x,y)
        self.food.setpos(self.food_xy)
 

    def initialize_game(self):
        self.gen_food_loc()




        while True:

            screen.update()
            time.sleep(0.1)
            #each frame needs to be generated here
            self.snakehead.prev = self.snakehead.pos()
            self.snakehead.forward(20)

            if not update_whole_snake(self.snakehead):
                #built in return for false return boolean meaning snake ate itself
                print(f'snake bit itself. final score = {self.score}')
                break
            #need a function to update all postions for all other snakes
            if are_positions_equal(self.snakehead.pos(),self.food.pos()):
                self.gen_food_loc()
                add_to_tail(self.snakehead)
                self.score+=1

            if self.check_gameover():
                print(f'went out of bounds. final score = {self.score}')
                break
            


            
    def check_gameover(self):
        # eats own tail 
        # goes out of bounds
        x = self.snakehead.pos()[0]
        y = self.snakehead.pos()[1]
        if x > 300 or x < -300 or y > 300 or y < -300:
            return True
        return False

            


def turn_right():
    game.snakehead.speed(0)
    game.snakehead.setheading(0)
    game.snakehead.speed(speed)

def turn_left():
    game.snakehead.speed(0)    
    game.snakehead.setheading(180)
    game.snakehead.speed(speed)

def turn_up():
    game.snakehead.speed(0)    
    game.snakehead.setheading(90)
    game.snakehead.speed(speed)

def turn_down():
    game.snakehead.speed(0)    
    game.snakehead.setheading(270)
    game.snakehead.speed(speed)

    


screen.listen()
game = SnakeGame()

screen.onkey(turn_right,'Right')
screen.onkey(turn_left,'Left')
screen.onkey(turn_up,'Up')
screen.onkey(turn_down,'Down')



game.initialize_game()




# Reference for Snake movement
# for _ in range(30):
#     snake.setheading(0)
#     snake.forward(20)
#     print(snake.pos())




screen.exitonclick()

