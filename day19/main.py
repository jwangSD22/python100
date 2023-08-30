from turtle import Turtle, Screen
from random import randint

screen = Screen()

black = Turtle()

red = Turtle()
orange = Turtle()
yellow = Turtle()
green = Turtle()
blue = Turtle()
violet = Turtle()
purple = Turtle()

turtles = [red, orange, yellow, green, blue, violet, purple]
colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
separation = [-225, -150, -75, 0, 75, 150, 225]

black.speed(20)
black.penup()
black.setpos(500, -275)
black.setheading(90)
black.pendown()
black.forward(600)
black.penup()


def check_turtles(turtles):
    for turtle in turtles:
        if turtle.xcor() >= 500:
            return True


# Initiate turtles into starting positions

for index in range(7):
    turtles[index].penup()
    turtles[index].shape("turtle")
    turtles[index].shapesize(3, 3)
    turtles[index].color(colors[index])
    turtles[index].setpos(-700, separation[index])
    turtles[index].speed(20)


selection = screen.textinput(
    title="Make your bet", prompt="Which color turtle are you going to bet on?"
)


winner = None

while not check_turtles(turtles):
    for turtle in turtles:
        turtle.forward(randint(0, 15))

for turtle in turtles:
    if turtle.xcor() >= 500:
        winner = turtle

print(f"{winner.color()[0]} turtle won the race!")
print(f"You bet on {selection}")

win_flag = None

if winner.color()[0] == selection.lower():
    win_flag = True
else:
    win_flag = False

if win_flag:
    print("YOU WIN!")
else:
    print("you lose...")


screen.exitonclick()
