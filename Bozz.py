import time
from time import sleep
import random
import turtle

def run_go():

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

def snake():

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

def calculator():
    math_type = input('Welcome to the BozzTR calculator! Choose: +, -, *, / ')
    if math_type == '+':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number + second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            restart = input('Continue to menu? yes/no ').lower()
            if restart == 'yes':
                main()
            else:
                exit()
    elif math_type == '-':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number - second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            restart = input('Continue to menu? yes/no ').lower()
            if restart == 'yes':
                main()
            else:
                exit()
    elif math_type == '*':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number * second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            restart = input('Continue to menu? yes/no ').lower()
            if restart == 'yes':
                main()
            else:
                exit()
    elif math_type == '/':
        first_number = int(input('First Number: '))
        second_number = int(input('Second number: '))
        sum = first_number / second_number
        print('Sum: ', sum)
        restart_calculator = input('Restart Calculator? y/n ')
        if restart_calculator == 'y':
            calculator()
        else:
            restart = input('Continue to menu? yes/no ').lower()
            if restart == 'yes':
                main()
            else:
                exit()

def pong():

    wn = turtle.Screen()
    wn.title('Pong')
    wn.bgcolor('black')
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Score
    score_a = 0
    score_b = 0

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape('square')
    paddle_a.color('white')
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.shape('square')
    paddle_b.color('white')
    paddle_b.shapesize(stretch_wid=5, stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('square')
    ball.color('white')
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = -0.2

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write('Player 1: 0  Player 2: 0', align='center', font=('Courier', 24, 'normal'))

    # Function
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
            y = paddle_b.ycor()
            y -= 20
            paddle_b.sety(y)

    # Keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, 'w')
    wn.onkeypress(paddle_a_down, 's')
    wn.onkeypress(paddle_b_up, 'Up')
    wn.onkeypress(paddle_b_down, 'Down')

    # Main game loop
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.setx(390)
            ball.goto(0, 0)
            score_a += 1
            pen.clear()
            pen.write('Player 1: {}  Player 2: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))
    
        if ball.xcor() < -390:
            ball.setx(390)
            ball.goto(0, 0)
            score_b += 1
            pen.clear()
            pen.write('Player 1: {}  Player 2: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
            ball.setx(-340)
            ball.dx *= -1

class rpsParticipant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper or scissor: ".format(name= self.name))
        print("{name} selects {choice}".format(name=self.name, choice = self.choice))
    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]
    def incrementPoint(self):
        self.points += 1
class rpsGameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]

        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        print("Round resulted in a {result} for Player 1".format(result = self.getResultAsString(result) ))
        if result > 0:
           p1.incrementPoint()
        elif result < 0:
           p2.incrementPoint()
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    def awardPoints(self):
        print("implement")
    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }       
        return res[result]

class rpsGame:
    def __init__(self):
        self.endGame = False
        self.participant = rpsParticipant("Player 1")
        self.secondParticipant = rpsParticipant("Player 2")
    def start(self):
        while not self.endGame:
            rpsGameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            rpsGameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points} point(s), and {p2name} has {p2points} point(s)".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString)

rpsGame = rpsGame()

def BA():
    BAl1 = input('Monster approaching! Demon👿! Do you: A, run away or B, attempt to shoot it out of the sky with rocks? ')
    if BAl1 == 'A':
        print('Good choice!')
    else:
        print('You threw the rocks, but they bounced off the demoms skin')
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()

startup = ['loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'Loading completed', '', 'starting .', 'starting ..', 'starting ...', '', 'starting .', 'starting ..', 'starting ...', '', 'starting .', 'starting ..', 'starting ...', '']

startMessage = input('Type start to begin loading BozzTR: ')

if startMessage == 'start':
    print('Loading BozzTR')

for stage in startup:
    print(stage)
    sleep(0.1)

print('Done')
nameMessage1 = input('What is your first name? ')
nameMessage2 = input('What is your last name? ')
print('Hello ' + nameMessage1 + ' ' + nameMessage2)


def main():

    begin = input('Type the task you want BozzTR to fufill or help to recieve help ')

    if begin == 'calculator':
        calculator()
    elif begin == 'help':
        print('Welcome to Bozz! Bozz is an interactive terminal to help you with everyday tasks like math or maybe you want some entertainment! type "commands" to see the full list of commands')
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'commands':
        print('''Here are all BozzTR commands:
        play: shows the game menu
        calculator: opens calculator
        help: displays help menu
        commands: shows this list'''
            )
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'play':
        gameMenu = input(nameMessage1 + ' ' + nameMessage2 + ', what do want to play? You can currently play: rps against friends (rps), BozzTR adventure (BA), pong (pong) ')
        if gameMenu == 'rps':
                rpsGame.start()
        elif gameMenu == 'BA':
            BAstart = input(nameMessage1 + ' ' + nameMessage2 + ' Welcome to the faraway land of Bozz! There is a mission waiting for you! Do you accept? yes/no ')
            if BAstart == 'yes':
                BA()
            else:
                print('wimp...')
                restart = input('Continue to menu? yes/no ').lower()
                if restart == 'yes':
                    main()
                else:
                    exit()
        elif gameMenu == 'snake':
            snake()
        elif gameMenu == 'run_go':
            run_go()
        elif gameMenu == 'run & go':
            run_go()
        elif gameMenu == 'pong':
            playPong = input('''Controls:
            player 1: w = up, s = down
            player 2: up arrow key = up, down arrow key = down
                                Start Pong? (y/n) ''')
            if playPong == 'y':
                
                pong()
            else:
                restart = input('Continue to menu? yes/no ').lower()
                if restart == 'yes':
                    main()
                else:
                    exit()
    else:
        print('Not a command')
        main()
main()