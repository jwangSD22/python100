import turtle

timmy = turtle.Turtle()

timmy.shape('turtle')
timmy.color('red')
timmy.forward(100)
timmy.back(100)

my_screen = turtle.Screen()
my_screen.onkey(lambda: timmy.forward(100), 'q')

my_screen.exitonclick()
