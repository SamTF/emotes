###### THE CLASSSICCC!! THE CLASSIC ###################################################
### Displays saved emote PNGs and GIFs

###### THE IMPORTS      ##########################################################
import discord
from discord.ext import commands
import os


print("_____________EmoteDealer INITIALISED_____________")

###### DISCORD STUFF ############################################################
### Creating the bot!

#The command prefix of all the commands
bot = commands.Bot(command_prefix='emote ')


### EVENTS ###
# Runs this when the bot becomes online
@bot.event
async def on_ready():
    print("Ready to spread some emotes!")
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game('Im back, baby'))   # custom status! (has a new syntax)



### THIS MAKES THE BOT REACT TO MESSAGES WITHOUT THE PREFIX
@bot.event
async def on_message(message):
    text = message.content.split()

    ## handles errors when there's no text
    try:
        emote = text[0]
    except IndexError:
        emote = "IndexError"

    
    # Only one-word commands are registered
    if len(text) > 1: return


    ### :D & D: - These two emotes are exceptions so we need to use an if statement to check for them
    if emote == "D:":
        await DealEmote(message, "D")
    
    elif emote == (":D"):
        await DealEmote(message, "FeelsAmazingMan")
    
    else:
        await DealEmote(message, emote)


### Actually gets the emote file and uploads it
async def DealEmote(message, emote, filetype = ".png"):
    # Checks if the emote exists as a PNG
    if (os.path.isfile(emote + ".png")):
        print("### Dealt a " + emote)

        await message.channel.send(file=discord.File(emote + ".png"))
        
    
    # Otherwise, check for GIFs
    elif (os.path.isfile(emote + ".gif")):
        print("### Dealt a " + emote)

        await message.channel.send(file=discord.File(emote + ".gif"))





#Runs the bot on the specified token
bot.run("NTY1Mjc5MzY4MzI3MjAwODIz.XK0JmA.JDmExmgchuerDJLrHW9XwttfRCM")




