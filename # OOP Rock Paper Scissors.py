# OOP Rock Paper Scissors - Callihan

class Participant: # Construct a model init method using points = 0 and choice = ""
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""
    def choose(self):
        self.choice = input("{name}, select rock, paper, or scissors: ".format(name=self.name))
        print("{name} selected {choice}")
    def toNumberChoice(self):
        switcher = {
            "rock":  0,
            "paper": 1, 
            "scissors": 2
        }
        def incrementPoint(self):
            self.points += 1
class GameRound:
    def __init__(self, p1, p2):
        p1.choose()
        p2.choose()
    def compareChoices(self):
        print("result")
    def awardPoints(self):
        print("result2")
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumberChoice()][p2.toNumberChoice()]
    def getResultAsString(self, result):
        res = {
            0: "Draw",
            1: "Win",
            -1: "Loss"
        }
        return res[result]
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print("This round resulted in a {result}".format (result = self.getResultAsString(result)))
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()
class Game: 
    def __init__(self):
        self.endgame = False
        self.Participant = Participant("Biff")
        self.secondParticipant = ("Marty")
    def start(self):
        game_round = GameRound(self.Participant, self.secondParticipant)
    def checkEndCondition(self):
        print("result3")
    def determineWinner(self):
        print("FinalResults")
    def determineWinner(self):
        resultsString = "It's a tie"
        if self.Participant.points > self.secondParticipant.points:
            resultsString = "The winner is {name}".format(name=self.Participant.name)
        elif self.Participant.points < self.secondParticipant.points:
            resultsString = "The winner is {name}".format(name=self.secondParticipant.name)
        print(resultsString)
game = Game()
game.start()
##
##  Logic Code
##
# if choice1 == "rock" and choice2 == "scissors":
    # return 1
# elif choice1 == "paper" and choice2 == "scissors":
    # return -1
# elif choice1 == "scissors" and choice2 == "scissors":
  #   return 0
# elif choice1 == "rock" and choice2 == "paper":
  #   return -1 
# elif choice1 == "scissors" and choice2 == "paper":
  #   return 1
# elif choice1 == "paper" and choice2 == "paper":
#     return 0
# elif choice1 == "paper" and choice2 == "rock":
  #   return 1
# elif choice1 == "scissors" and choice2 == "rock":
  #   return -1
# elif choice1 == "rock" and choice2 == "rock":
 #    return 0
 # What were the choices and who won?
#############
# Easier Way
# rules = [
# [0, -1, 1],
# [1, 0, -1],
# [-1, 1, 0]
# ]
# rules[0][1]
##############