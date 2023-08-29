from turtle import Turtle
from turtle import Screen
from random import randint, choice

timmy = Turtle()
timmy.shape('turtle')
screen = Screen()
screen.colormode(255)


## draw multiple shapes
# for x in range(8):
#     color_tuple_1 = (randint(0,255)/255,randint(0,255)/255,randint(0,255)/255)
#     color_tuple_255 = (randint(0,255),randint(0,255),randint(0,255))
#     timmy.pencolor(color_tuple_255)
#     for _ in range(3 + x):
#         timmy.forward(100)
#         timmy.right(360 / (3 + x))

def random_walk():
    timmy.width(15)
    timmy.speed(20)
    multiplier = [0,1,2,3]
    for _ in range(200):
        color_tuple_255 = (randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.pencolor(color_tuple_255)
        timmy.forward(65)
        timmy.setheading(90 * (choice(multiplier)))

def spirograph():




random_walk()

screen.exitonclick()
