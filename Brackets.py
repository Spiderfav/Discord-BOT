import pickle
import random
import discord

with open("contestants.txt", "rb") as fp:
    local_contestants = pickle.load(fp)

if len(local_contestants) % 2 != 0:
    a = random.choice(local_contestants)
    local_contestants.pop(a)
    b = random.choice(local_contestants)
    local_contestants.pop(b)
    await message.channel.send(a+" VS "+B)
    
