from turtle import Turtle
from turtle import Screen
from random import randint, choice
import colorgram
from PIL import Image

import os

# Get the directory containing the script
# IS THIS THE SAME CASE ON UNIX BASED OS? 
# IS THIS A WINDOWS ONLY PROBLEM?
script_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = "color_test.jpg"
absolute_path = os.path.join(script_directory, relative_path)

print(absolute_path)

my_img = Image.open(absolute_path)
    
my_colors = colorgram.extract(my_img,40)
color_array = []
for color in my_colors:
    color_array.append(color.rgb)

print(color_array)


timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)


# draw multiple shapes
# for x in range(8):
#     color_tuple_1 = (randint(0,255)/255,randint(0,255)/255,
#       randint(0,255)/255)
#     color_tuple_255 = (randint(0,255),randint(0,255),randint(0,255))
#     timmy.pencolor(color_tuple_255)
#     for _ in range(3 + x):
#         timmy.forward(100)
#         timmy.right(360 / (3 + x))


def random_walk():
    timmy.width(15)
    timmy.speed(20)
    multiplier = [0, 1, 2, 3]
    for _ in range(200):
        color_tuple_255 = (randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.pencolor(choice(color_array))
        timmy.forward(65)
        timmy.setheading(90 * (choice(multiplier)))

 
# random_walk()

def spirograph():
    timmy.speed(20)
    for _ in range (72):
        color_tuple_255 = (randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.pencolor(choice(color_array))
        timmy.circle(100)
        timmy.right(5)


# spirograph()

def hirst():

    x = -250
    y = -300
    
    timmy.speed(20)
    timmy.penup()
    for _ in range(10):
        y+=50
        timmy.setpos(x,y)
        for _ in range (10):
            timmy.pencolor(choice(color_array))
            timmy.dot(20)
            timmy.forward(50)




hirst()


screen.exitonclick()
