from turtle import Turtle

snake = Turtle()
snake.penup()
snake.shape('square')
snake.shapesize(1,1)
snake.color('white')
snake.val = (0,0)
snake.next = None
snake.speed(2)

food = Turtle()
food.shape('square')
food.shapesize(1,1)
food.color('red')
food.speed(0)
food.penup()
