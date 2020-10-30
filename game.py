'''
Program that runs the snake game
Manuel Barrera Lopez Portillo A01570669
30/10/2020
'''

#Importing the libraries for the game. MAKE SURE TO INSTALL THEM ALL BEFORE RUNNING
from turtle import *
from random import randrange
from freegames import square, vector
#Initial position of the snake
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Definition of the snake direction
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
#Definition of the snake head position and how it should move
def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
#Definition of the snake movement related to the keys in keyboard
def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    #Definition of position of the snake and how it can move outside the box
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    #Increase of snake length
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    #Color of the snake and food
    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

#Initial parameters
setup(500, 500, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
