import discord
import random
import time
import datetime

from tkinter import *

intents = discord.Intents.all()

client = discord.Client(intents=intents)

fight = 0

@client.event
async def on_ready():
    print(f'The meenotaur has arrived.')

@client.event
async def on_message(message):
    global fight
    activationArr = ["minotaur", "meenotaur"]
    if message.author == client.user:
        return

    if fight == 1:
        return
    
    activate = 0
    for string in activationArr:
        if message.content.lower().find(string.lower()) > -1:
            activate = 1
            break

    randActivate = random.randint(0, 300)
    if (activate == 1):
        fight = 1
        fighter = message.author
        await message.channel.send('The meenotaur\'s heavy footfalls shake the ground as it enters ' + message.channel.name + ".")

        time.sleep(5)

        await battle(fighter, message.channel)

async def battle(fighter, channel):
    global fight

    attackArr = ["Beheading swing!", "Overhead Crush!", "Gores You!", "\\*wiggles pinky\\*", "Bullfist!", "Flatten!"]
    counterArr = ["duck", "sidestep", "jump", "\\*wiggle\\*", "block", "dive"]
    mathMessage = "The meenotaur holds up a sheet of paper. "
    health = 99
    chance = 6

    while health > 0:
        randomAttack = random.randint(0, 100)
        currIndex = random.randint(0, len(attackArr) - 1)
        currAttack = attackArr[currIndex]
        currCounter = counterArr[currIndex]

        match randomAttack:
            case 100:
                num1 = random.randint(1, 10000)
                num2 = random.randint(1, 10000)
                operator = random.randint(0, 3)

                match operator:
                    case 0:
                        currAttack = mathMessage + str(num1) + " + " + str(num2)
                        currCounter = str(num1 + num2)
                    case 1:
                        currAttack = mathMessage + str(num1) + " - " + str(num2)
                        currCounter = str(num1 - num2)
                    case 2:
                        currAttack = mathMessage + str(num1) + " * " + str(num2)
                        currCounter = str(num1 * num2)
                    case 3:
                        currAttack = mathMessage + str(num1) + " / " + str(num2)
                        currCounter = str(num1 / num2)

            case 98:
                currAttack = "The meenotaur stops and stares at you."
                currCounter = ".........."

        await channel.send(currAttack)

        time.sleep(chance)

        messages = [message async for message in channel.history()]
        
        i = 0
        while messages[i].content.lower() != currCounter:
            if messages[i].content == currAttack:
                try:
                    await fighter.timeout(datetime.timedelta(minutes=(health)), reason = "The meenotaur got you.")
                    defeat = fighter.name + " was killed by the meenotaur."
                    await channel.send(content=defeat)
                    fight = 0
                    return   
                except:
                    defeatNoPerms = "The minotaur knocks " + fighter.name + " to the ground and walks away. (Doesn't have permissions to time out " + fighter.name + ")"
                    await channel.send(content=defeatNoPerms)
                    fight = 0
                    return
            i += 1   
        
        health -= 1

        if (health % 20 == 0):
            await channel.send("The meenotaur's blood begins to boil.")
            chance -= 1

    await channel.send("The meenotaur falls to the ground as it exhales it's final breath.")
    quit()

client.run('TOKEN HERE')