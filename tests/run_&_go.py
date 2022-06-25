import turtle
import random
import time

wn = turtle.Screen()
wn.title('Run & Go')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0)

enemy_speed = 15

enemies = []

score = 0

text = turtle.Turtle()
text.speed(0)
text.shape('square')
text.color('white')
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write('Move the ammo to the red square', align='center', font=('Courier', 24, 'normal'))

# Player
player = turtle.Turtle()
player.speed(0)
player.shape('square')
player.color('white')
player.penup()
player.goto(0, 0)

# Ammo
ammo = turtle.Turtle()
ammo.speed(0)
ammo.shape('square')
ammo.turtlesize(0.5)
ammo.color('yellow')
ammo.penup()
ammo.goto(0, 0)

# Start
start = turtle.Turtle()
start.speed(0)
start.shape('square')
start.color('red')
start.penup()
start.goto(0, 80)

# Enemy
enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape('square')
enemy.color('grey')
enemy.penup()
enemy.hideturtle()
enemy.goto(0, 80)

# Function
def player_up():
    y = player.ycor()
    y += 20
    player.sety(y)

def player_down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def player_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def player_right():
    x = player.xcor()
    x += 20
    player.setx(x)

def ammo_up():
    y = ammo.ycor()
    y += 20
    ammo.sety(y)

def ammo_down():
    y = ammo.ycor()
    y -= 20
    ammo.sety(y)

def ammo_left():
    x = ammo.xcor()
    x -= 20
    ammo.setx(x)

def ammo_right():
    x = ammo.xcor()
    x += 20
    ammo.setx(x)

wn.listen()
wn.onkeypress(player_up, 'w')
wn.onkeypress(player_left, 'a')
wn.onkeypress(player_down, 's')
wn.onkeypress(player_right, 'd')
wn.onkeypress(ammo_up, 'Up')
wn.onkeypress(ammo_down, 'Down')
wn.onkeypress(ammo_left, 'Left')
wn.onkeypress(ammo_right, 'Right')
wn.onkeypress(wn.bye, 'q')


while True:
    wn.update()

    if enemy.distance(ammo) < 20:
        enemy.goto(random.randint(-290, 290), random.randint(-290, 290))
        text.clear()
        text.write('Score: {}'.format(score), align='center', font=('Courier', 24, 'normal'))
        score += 1

    if enemy.distance(player) < 20:
        text.clear()
        text.write('Game Over', align='center', font=('Courier', 24, 'normal'))
        time.sleep(3)
        wn.bye()
    
    if ammo.distance(start) < 20:
        start.goto(1000, 1000)
        enemy.showturtle()
        enemy.goto(random.randint(-290, 290), random.randint(-290, 290))
        enemies.append(enemy)
        text.clear()
        text.write('Move ammo to gray square', align='center', font=('Courier', 24, 'normal'))
        def follow_player():
            enemy.setheading(enemy.towards(player))
            enemy.forward(1)
            wn.ontimer(follow_player, enemy_speed)

        follow_player()
        