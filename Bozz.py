def calculator():
    math_type = input('Welcome to the calculator! Choose: +, -, *, / ')
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

    import turtle

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
    
from io import open_code
from time import sleep

startup = ['loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'Loading completed', '', 'starting .', 'starting ..', 'starting ...', '', 'starting .', 'starting ..', 'starting ...', '', 'starting .', 'starting ..', 'starting ...', '']

startMessage = input('Type start to begin loading Bozz: ')

if startMessage == 'start':
    print('Loading Bozz')

for stage in startup:
    print(stage)
    sleep(0.1)

print('Done')
nameMessage1 = input('What is your first name? ')
nameMessage2 = input('What is your last name? ')
print('Hello ' + nameMessage1 + ' ' + nameMessage2)


def main():

    begin = input('Type the task you want Bozz to fufill or help to recieve help ')

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
        print('''Here are all Bozz commands:
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
        gameMenu = input(nameMessage1 + ' ' + nameMessage2 + ', what do want to play? You can currently play: rps against friends (rps), Bozz adventure (BA), pong (pong) ')
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
main()