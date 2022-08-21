# Firstly, import the modules needed for the game: turtle, random and time.
import turtle
import random
import time

# define the values
lives = 3
score = 0


# Set up the window that will appear on screen (test)
window = turtle.Screen()
window.tracer(0)
window.title('Turtle ')
window.bgcolor('light blue')
window.setup(800,800)

# Define the turtle icon
t = turtle.Turtle()
t.speed(0)
t.penup()
t.color('green')
t.shape('turtle')
t.direction = 'stop'
t.shapesize(stretch_wid=3, stretch_len=3)

# Define the list for predators that will hunt the turtles
predators = []
for x in range(10):
    predator = turtle.Turtle()
    predator.penup()
    predator.color('red')
    predator.shape('circle')
    predator.shapesize(stretch_wid=1.3, stretch_len=1.3)
    predator.speed = 0.5
    x = random.randint(-380,380)
    y = random.randint(-380, 380)
    predator.setposition(x,y)
    predators.append(predator)

pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.goto(0,320)
pen.pendown()
pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 20))
pen.hideturtle()

# Define the fish (food that the turtles eat)
fish = []
for _ in range(40):
    f = turtle.Turtle()
    f.speed(0)
    f.penup()
    f.color('dark blue')
    f.shape('circle')
    f.shapesize(stretch_wid=1, stretch_len=1)
    x = random.randint(-380,380)
    y = random.randint(-380, 380)
    f.setposition(x,y)
    fish.append(f)

# Define the movements of the turtles
def movement():
    if t.direction == 'up':
        y = t.ycor()
        y+= 0.7
        t.sety(y)

    if t.direction == 'down':
        y = t.ycor()
        y-= 0.7
        t.sety(y)

    if t.direction == 'left':
        x = t.xcor()
        x-= 0.7
        t.setx(x)

    if t.direction == 'right':
        x = t.xcor()
        x+= 0.7
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


# Set window bindings
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


    # Border collision
    if t.xcor()>390 or t.xcor()<-390 or t.ycor()>390 or t.ycor()<-390 :
        lives-= 1
        pen.clear()
        pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 20))
        time.sleep(1)
        t.goto(0,0)


    # Check Lives
    if lives == 0:
        score=0
        lives=3
        pen.clear()
        pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 20))
        time.sleep(1)
        t.goto(0,0)


    # Food and Turtle collision
    for f in fish:
        if t.distance(f) < 10:
            score+=1
            pen.clear()
            pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 20))
            x = random.randint(-380, 380)
            y = random.randint(-380, 380)
            f.goto(x,y)


    # Prdeator and border
    for predator in predators:
        if predator.xcor()>390 or predator.xcor()<-390 or predator.ycor()>390 or predator.ycor()<-390:
            x = random.randint(-380, 380)
            y = random.randint(-380, 380)
            predator.goto(x,y)
            predatorMovement()

    # predator and turtle collison
    for predator in predators:
        if t.distance(predator) < 10:
            lives -=1
            pen.clear()
            pen.write('HUNGRY TURTLE POINTS: {}                 LIVES: {}'.format(score, lives), align='center', font=('Comic Sans MS', 20))
            time.sleep(1)
            t.goto(0, 0)



    movement()
    predatorMovement()


delay = raw_input('Press enter to finish')