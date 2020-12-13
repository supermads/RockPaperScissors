# Write your code here
import random


def rps(player, computer):
    if player not in ["rock", "paper", "scissors"]:
            print("Invalid input")
    elif (player == "rock" and computer == "paper") or (player == "paper" and computer == "scissors") or (player == "scissors" and computer == "rock"):
        print("Sorry, but the computer chose {}".format(computer))
    elif player == computer:
        print("There is a draw ({})".format(player))
        return 50
    else:
        print("Well done. The computer chose {} and failed".format(computer))
        return 100
    return 0


name = input("Enter your name: ")
print("Hello, {}".format(name))
options = input().split(",")
n = len(options)
print("Okay, let's start")
score = 0
keep_going = True
records = {}
f = open("rating.txt", "r")
for line in f:
    (key, val) = line.split()
    records[key] = val
if name in records:
    score = int(records.get(name))
f.close()
while keep_going:
    player = input()
    if player == "!exit":
        print("Bye!")
        keep_going = False
    elif player == "!rating":
        print("Your rating: {}".format(score))
    elif options == ['']:
        rpsoptions = ["rock", "paper", "scissors"]
        computer = rpsoptions[random.randint(0,2)]
        score += rps(player, computer)
    else:
        computer = options[random.randint(0,(n - 1))]
        ranks = []
        if player not in options:
            print("Invalid input")
        for option in options:
            if option != player:
                ranks.append(option)
        place = ranks.index(computer)
        if player == computer:
            print("There is a draw ({})".format(player))
            score += 50
        elif place > (len(ranks) / 2):
            print("Sorry, but the computer chose {}".format(computer))
        else:
            print("Well done. The computer chose {} and failed".format(computer))
            score += 100
    


