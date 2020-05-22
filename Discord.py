import discord
import asyncio
import pickle

with open("contestantsID.txt", "rb") as fp:
    local_contestantsID = pickle.load(fp)

with open("contestants.txt", "rb") as fp:
    local_contestants = pickle.load(fp)

commands = ["register","unregister","help","players"]
commands_text = ["Used followed by name like '>register PlayerName'","Used followed by name like '>unregister PlayerName'","Gives a list of commands","Give a list of players in tournaments"]

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----------')


@client.event
async def on_message(message):
    b = message.author.id
    if message.content.startswith('>register'):
        if len(local_contestants) == 16:
            await message.channel.send("The tournament is full right now!")

        else:
            m = message.content.split()
            try:
                a = m[1].upper()
                await message.channel.send(a+", will be your name in the tournament!")
                local_contestants.append(a)
                local_contestantsID.append(b)
                with open("contestants.txt", "wb") as fp:
                    pickle.dump(local_contestants, fp)

                with open("contestantsID.txt", "wb") as fp:
                    pickle.dump(local_contestantsID, fp)

            except:
                await message.channel.send("You did not give me a name!")

    elif message.content.startswith('>unregister'):
        m = message.content.split()

        try:
            a = m[1].upper()

            for x in range(0,len(local_contestants)):
                if local_contestants[x] == a:
                    if message.author.id == local_contestantsID[x]:
                        local_contestants.pop(x)
                        local_contestantsID.pop(x)


                        with open("contestants.txt", "wb") as fp:
                            pickle.dump(local_contestants, fp)

                        with open("contestantsID.txt", "wb") as fp:
                            pickle.dump(local_contestantsID, fp)

                        await message.channel.send("Done!")

                    else:
                        await message.channel.send("That is not your registration!")

        except:
            await message.channel.send("You did not give me a name!")


    elif message.content.startswith('>help'):
        for i in range(0,len(commands)):
            await message.channel.send(commands[i])
            await message.channel.send(commands_text[i])
            await message.channel.send("-------------")

    elif message.content.startswith('>players'):

        await message.channel.send("Currently, there are "+ str(len(local_contestants)) +" players in the tournament:")

        for i in range(0,len(local_contestants)):
            await message.channel.send(local_contestants[i])

    elif message.content.startswith('>purge'):
        if message.author.id == 340610417967497216 or message.author.id == 364830006334980096:
            local_contestants.clear()
            local_contestantsID.clear()

            with open("contestants.txt", "wb") as fp:
                pickle.dump(local_contestants, fp)

            with open("contestantsID.txt", "wb") as fp:
                pickle.dump(local_contestantsID, fp)

            await message.channel.send("Done!")

    elif message.content.startswith('>delete'):
        if message.author.id == 340610417967497216 or message.author.id == 364830006334980096:
            m = message.content.split()
            a = m[1].upper()

            for l in range(0,len(local_contestants)):
                if local_contestants[l] == a:
                    local_contestants.pop(l)
                    local_contestantsID.pop(l)


                    with open("contestants.txt", "wb") as fp:
                        pickle.dump(local_contestants, fp)

                    with open("contestantsID.txt", "wb") as fp:
                        pickle.dump(local_contestantsID, fp)

                    await message.channel.send("Done!")

    elif message.content.startswith('>data'):
        if message.author.id == 340610417967497216 or message.author.id == 364830006334980096:
            await message.channel.send(local_contestants)
            await message.channel.send(local_contestantsID)

    elif message.content.startswith('>timer'):
        await message.channel.send("Tournaments are held every Friday at 5:00 PM BST.")




f = open("env.txt", "r")
contents = f.read()
client.run(contents)
