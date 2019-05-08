import discord
from discord.ext import commands
import random
import diceHandler

requesttoken = open("botcommand.txt", "r").read()
token = open("token.txt", "r").read()  # Token Information
description = '''Mac's Brainchild,
the Pun Boat'''
bot = commands.Bot(command_prefix=requesttoken, description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    statusnotifi = discord.Game("with your bad puns") #setup a custom game
    await bot.change_presence(status=discord.Status.online, activity=statusnotifi, afk=False) #Set bot status as the custom game, online, afk not possible.
    print('------')

@bot.command(description="Get some jokes of any kind")
async def joke(ctx):
     """Provides a regular joke"""
     lines = open("jokes.txt").read().split("|")
     myline = random.choice(lines)
     await ctx.send(myline)

@bot.command(description="Get only some dadjokes")
async def dadjoke(ctx):
    """Provide's a dadjoke"""
    lines = open("dadjokes.txt").read().splitlines()
    myline = random.choice(lines)
    await ctx.send(myline)

@bot.command(description="Set the request token")
async def setrequesttoken(ctx, index: str):
    """Set's the request token"""
    if ctx.message.author.Permissions.administrator:
        await ctx.send("Successfully changed the bot token")
        requesttoken = open("botcommand.txt", "w")
        requesttoken.write(index)
        requesttoken.close()
    else:
        await ctx.send("Not Enough Permissions")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in <num>d<sides>format"""
    results = """The results from your role were
    {0}

    The following stastics were observed:
    Average: {1}
    Lowest: {2}
    Highest: {3}
    Total: {4}
    Median: {5}
    Mode: {6}

    """
    d = diceHandler.diceHandle(dice)
    await ctx.send("Debug: "+str(d)+"\n"+results.format(d["rolls"], d["average"], d["lowest"], d["highest"], d["total"], d["median"], d["mode"]))

@bot.command(description="Info")
async def botinfo(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, I really am a Boat, and I am really Punny.')

def imdad(messagecontent, messageauthorname):
         afterim = "".split("im broken" , 1)
         dadname = open("dadname.txt", "r").read()
         #lets get there spelling of i'm
         if " i'm " in messagecontent:
          afterim = messagecontent.split("i'm", 1)
         if " I'm " in messagecontent:
          afterim = messagecontent.split("I'm", 1)
         if " im " in messagecontent:
          afterim = messagecontent.split("im", 1)
         if messageauthorname == "Pun Boat":
            return ""
         if afterim[0] == "":
             return "Hi "+messageauthorname+", I'm "+dadname
         if afterim[1] == "":
             return "Hi "+afterim[2]+", I'm "+dadname
         else:
            return "Hi "+afterim[1]+", I'm "+dadname
@bot.event
async def on_message(message):
    if " i'm " in message.content.lower():
        if imdad(message.content, message.author.name) == "":
            return
        else: 
            await message.channel.send(imdad(message.content, message.author.name))
    if " im " in message.content.lower():
        if imdad(message.content, message.author.name) == "":
            return
        else: await message.channel.send(imdad(message.content, message.author.name))

    await bot.process_commands(message)

bot.run(token)