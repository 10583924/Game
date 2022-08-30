# Firstly, import the modules needed for the game: turtle, random and time.
import turtle
import random
import time


# Define the values of the number of lives and the starting score count
lives = 3
score = 0
high_score = 0

# Set up the window that will appear on screen when you press run
# inluding the background image of the game
window = turtle.Screen()
window.tracer(0)
window.title('Turtle')
window.bgcolor('#34ebd5')
window.bgpic("under_the.gif")
window.setup(1000,1000)

# Define the turtle icon, size and colour
t = turtle.Turtle()
t.speed(0)
t.penup()
t.color('green')
t.shape('turtle')
t.direction = 'stop'
t.shapesize(stretch_wid=3, stretch_len=3)

# Define the list for predators that will hunt the turtles and their size and colour
predators = []
for x in range(10):
    predator = turtle.Turtle()
    predator.penup()
    predator.color('red')
    predator.shape('circle')
    predator.shapesize(stretch_wid=1, stretch_len=1)
    predator.speed = 0.5
    x = random.randint(-480,480)
    y = random.randint(-480, 480)
    predator.setposition(x,y)
    predators.append(predator)

# Define the score and lives to be visible on the top of the screen throughout the game
pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.goto(0,420)
pen.pendown()
pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 30))
pen.penup()
pen.hideturtle()



# Define the fish (the food that the turtles eat) and their size and colour
fish = []
for _ in range(40):
    f = turtle.Turtle()
    f.speed(0)
    f.penup()
    f.color('yellow')
    f.shape('triangle')
    f.shapesize(stretch_wid=1, stretch_len=1)
    x = random.randint(-480,480)
    y = random.randint(-480, 480)
    f.setposition(x,y)
    fish.append(f)

# Define the movements of the turtles. a.k.a the event handlers.
def movement():
    if t.direction == 'up':
        y = t.ycor()
        y+= 1.5
        t.sety(y)

    if t.direction == 'down':
        y = t.ycor()
        y-= 1.5
        t.sety(y)

    if t.direction == 'left':
        x = t.xcor()
        x-= 1.5
        t.setx(x)

    if t.direction == 'right':
        x = t.xcor()
        x+= 1.5
        t.setx(x)


# Define predator movement
def predatorMovement():
    for predator in predators:
        y = predator.ycor()
        x = predator.xcor()
        y += predator.speed
        x += predator.speed
        predator.sety(y)
        predator.setx(x)

# Window Bindings functions
def moveUp():
    t.direction ='up'

def moveDown():
    t.direction = 'down'

def moveLeft():
    t.direction = 'left'

def moveRight():
    t.direction = 'right'

def start_game():
    global game_state
    game_state = "game"


# Set window bindings and the functionality of the keypresses
# Set up the window to listen for the event handlers.
window.listen()
window.onkeypress(moveUp, 'Up')
window.onkeypress(moveDown, 'Down')
window.onkeypress(moveLeft, 'Left')
window.onkeypress(moveRight, 'Right')


# - - - - - - - - - - - - - - - - - - - - - - #
# Main Game Loop
# - - - - - - - - - - - - - - - - - - - - - - #

while True:
    window.update()


    # Border collision to determine the sides of the game
    if t.xcor()>490 or t.xcor()<-490 or t.ycor()>490 or t.ycor()<-490 :
        lives-= 1
        pen.clear()
        pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 30))
        pen.penup()
        time.sleep(1)
        t.goto(0,0)


    # Check the number of lives left
    if lives == 0:
        score=0
        lives=3
        pen.clear()
        pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 30))
        pen.penup()
        time.sleep(3)
        t.goto(0,0)


    # Food and Turtle collision
    for f in fish:
        if t.distance(f) < 10:
            score+=1
            pen.clear()
            pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 30))
            pen.penup()
            x = random.randint(-480, 480)
            y = random.randint(-480, 480)
            f.goto(x,y)


    # Prdeator and border
    for predator in predators:
        if predator.xcor()>490 or predator.xcor()<-490 or predator.ycor()>490 or predator.ycor()<-490:
            x = random.randint(-480, 480)
            y = random.randint(-480, 480)
            predator.goto(x,y)
            predatorMovement()

    # predator and turtle collison
    for predator in predators:
        if t.distance(predator) < 10:
            lives -=1
            pen.clear()
            pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 30))
            pen.penup()
            time.sleep(1)
            t.goto(0, 0)


    movement()
    predatorMovement()

