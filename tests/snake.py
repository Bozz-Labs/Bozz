import turtle
import time
import random

delay = 0.1

# Screen setup

wn = turtle.Screen()
wn.title('Snake')
wn.bgcolor('black')
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('red')
food.penup()
food.goto(0, 100)

segments = []



# Functions
def go_up():
    head.direction = 'up'
def go_down():
    head.direction = 'down'

def go_left():
    head.direction = 'left'

def go_right():
    head.direction = 'right'
def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)
    
    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
    
    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
    
    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'w')
wn.onkeypress(go_down, 's')
wn.onkeypress(go_left, 'a')
wn.onkeypress(go_right, 'd')

# Main game loop
while True:
    wn.update()

    # Check for collision with border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear segments list
        segments = []

    # Check for collision with food

    if head.distance(food) < 20:
        # Move food
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)

    # Move end segment first
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # Move segment 0 to snake head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    time.sleep(delay)

wn.mainloop()