import pickle
import random


with open("contestants.txt", "rb") as fp:
    local_contestants = pickle.load(fp)

winners = []

def decide_winner():

    winner = input("Announce Winner: ")

    if winner.upper() == player1:
        winners.append(player1)

    elif winner.upper() == player2:
        winners.append(player2)

    else:
        print("Please try again.")
        decide_winner()


def bracket_generator():
    while len(local_contestants) != 0:
        a = random.randint(0,len(local_contestants)-1) # Gives me player name
        player1 = local_contestants[a]
        local_contestants.pop(a)

        b = random.randint(0,len(local_contestants)-1) # Gives me player name
        player2 = local_contestants[b]
        local_contestants.pop(b)

        print(player1+" VS "+player2)

        decide_winner()

    else:

        for i in range(0,len(winners)):
            local_contestants.append(winners[i])

        winners.clear()

bracket_generator()
