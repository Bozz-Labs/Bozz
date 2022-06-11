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
startMessage = input('Type start to begin loading Bozz: ')

if startMessage == 'start':
    print('Loading Bozz')

from os import kill
    
from time import sleep

startup = ['loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'loading .', 'loading ..', 'loading ...', '', 'Loading completed', '', 'starting .', 'starting ..', 'starting ...', '', 'starting .', 'starting ..', 'starting ...', '', 'starting .', 'starting ..', 'starting ...', '']

for stage in startup:
    print(stage)
    sleep(0.1)
print('completed')

nameMessage1 = input('What is your first name? ')
nameMessage2 = input('What is your last name? ')
print('Hello ' + nameMessage1 + ' ' + nameMessage2)

def main():

    begin = input('Type the task you want Bozz to fufill or help to recieve help ')

    if begin == 'addition':
        first_number = int(input('First number: '))
        second_number = int(input('Second number: '))
        print("Sum: ", first_number + second_number)
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'subtrction':
        first_number = int(input('First number: '))
        second_number = int(input('Second number: '))
        print("Sum: ", first_number - second_number)
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'multiplication':
        first_number = int(input('First number: '))
        second_number = int(input('Second number: '))
        print("Sum: ", first_number * second_number)
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'division':
        first_number = int(input('First number: '))
        second_number = int(input('Second number: '))
        print("Sum: ", first_number / second_number)
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'help':
        print('Welcome to Bozz! Bozz is an interactive task manager to help you with everyday tasks like math or maybe you want some entertainment! type "commands" to see the full list of commands')
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'commands':
        print('Here is a list of commands: \
            addition: Whole number addition\
            subtraction: Whole number subtraction\
            multiplication: Whole number multiplication\
            division: Whole number division\
            play: displays the game menu\
            commands: displays this list\
            help: displays the help menu'
            )
        restart = input('Continue to menu? yes/no ').lower()
        if restart == 'yes':
            main()
        else:
            exit()
    elif begin == 'play':
        gameMenu = input(nameMessage1 + ' ' + nameMessage2 + ', what do want to play? You can currently play: rps against friends (rps), Bozz adventure (BA) ')
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

main()
