import random
import discord
import asyncio
from discord.context_managers.commands import Bot

requesttoken = open("botcommand.txt", "r").read()
token = open("token.txt", "r").read()  # Token Information

client = Bot(description="Play's With Your Bad Puns", command_prefix=requesttoken, pm_help = True, )

@client.event
async def on_ready():  
    print(f'We have logged in as {client.user}') #Log Login on console
    statusnotifi = discord.Game("with your bad puns") #setup a custom game
    await client.change_presence(status=discord.Status.online, activity=statusnotifi, afk=False) #Set bot status as the custom game, online, afk not possible.

@client.command()
async def joke(ctx):
     lines = open("jokes.txt").read().split("|")
     myline = random.choice(lines)
     await ctx.send(myline)

@client.command()
async def dadjoke(ctx):
    lines = open("dadjokes.txt").read().splitlines()
    myline = random.choice(lines)
    await ctx.send(myline)

@client.command()
async def setrequesttoken(ctx, index: int):
    if ctx.message.author.server_permissions.administrator:
        await ctx.send("Successfully changed the bot token")
        requesttoken = open("botcommand.txt", "w")
        requesttoken.write(ctx.message)
        requesttoken.close()

def setrequesttoken(messagecontent, messageauthorname, administratorstatus):
    if messageauthorname == "Pun Boat":
        return ""
    if administratorstatus == False:
        return ""
    newtoken = messagecontent.split()
    print("Setting new Token:"+ str(newtoken)+"\n The permission level of "+messageauthorname+" is "+administratorstatus+": Administrator")
    requesttoken = open("botcommand.txt", "w")
    requesttoken.write(newtoken[1])
    requesttoken.close()

def copypasta(messagecontent, messaugeauthorname):
    if messageauthorname == "Pun Boat":
        return ""
    lines = open("copypasta.txt").read().splitlines()
    myline = random.choice(lines)
    return myline
def providehelp(messagecontent, messageauthorname):
    if messageauthorname == "Pun Boat":
        return ""
    lines = open("help.txt").read()
    return lines

@client.event  #catch the event decorator
async def on_ready():  
    print(f'We have logged in as {client.user}') #Log Login on console
    statusnotifi = discord.Game("with your bad puns") #setup a custom game
    await client.change_presence(status=discord.Status.online, activity=statusnotifi, afk=False) #Set bot status as the custom game, online, afk not possible.
@client.event
async def on_message(message):  # event that happens per any message.
    # console log messages (DEBUG)
    print(f"{message.channel} -> {message.author}: {message.content}")
    #
    if "i'm" in message.content.lower():
        if imdad(message.content, message.author.name) == "":
            return
        else: 
            await message.channel.send(imdad(message.content, message.author.name))
    if "im" in message.content.lower():
        if imdad(message.content, message.author.name) == "":
            return
        else: await message.channel.send(imdad(message.content, message.author.name))
    #get joke
    
    if requesttoken+"dadjoke" in message.content.lower():
        if returnjoke(message.content, message.author.name) == "":
            return
        else:
            await message.channel.send(returnjoke(message.content, message.author.name))
    if requesttoken+"setrequesttoken" in message.content.lower():
        if setrequesttoken(message.content, message.author.name, ) == "":
            return
        else:
            setrequesttoken(message.content, message.author.name, )
            await message.channel.send("New Bot Command Token Succesfully Set")
    if requesttoken+"copypasta" in message.content.lower():
        if copypasta(message.content, message.author.name) == "":
            return
        else:
            await message.channel.send(copypasta(message.content, message.author.name))
    if requesttoken+"help" in message.content.lower():
        if providehelp(message.content, message.author.name) == "":
            return
        else:
            await message.channel.send(providehelp(message.content, message.author.name))
    if requesttoken+"joke" in message.content.lower():
        if joke(message.content, message.author.name) == "":
            return
        else:
            await message.channel.send(joke(message.content, message.author.name))

client.run(token)  # Execute Bot
