import pickle

player = ["Spiderfav"]

with open("contestants.txt", "wb") as fp:
    pickle.dump(player, fp)
