from platform import java_ver
import turtle
import time
import random

def snake():

    delay = 0.1
    
    score = 0

    high_score = 0

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
    
    # Score Text
    score_text = turtle.Turtle()
    score_text.speed(0)
    score_text.shape('square')
    score_text.color('white')
    score_text.penup()
    score_text.hideturtle()
    score_text.goto(0, 260)
    score_text.write('Score: 0  High Score: 0', align='center', font=('Courier', 24, 'normal'))


    # Functions
    def go_up():
        if head.direction != 'down':
            head.direction = 'up'

    def go_down():
        if head.direction != 'up':
            head.direction = 'down'

    def go_left():
        if head.direction != 'right':
            head.direction = 'left'

    def go_right():
        if head.direction != 'left':
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
            for segment in segments:
                segment.goto(1000, 1000)
                delay = 0.1
                score = 0
                score_text.clear()
                score_text.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))


            # Clear segments
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
            delay -= 0.001
            score += 1

            if score > high_score:
                high_score = score
            
            score_text.clear()
            score_text.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))

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

        # Check for collision with segment
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = 'stop'
                for segment in segments:
                    segment.goto(1000, 1000)
                    delay = 0.1
                    score = 0
                    score_text.clear()
                    score_text.write('Score: {}  High Score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))


                # Clear segments
                segments = []

        time.sleep(delay)

    wn.mainloop()

snake()