###### THE CLASSSICCC!! THE CLASSIC ###################################################
### Displays saved emote PNGs and GIFs

###### THE IMPORTS      ##########################################################
import discord
from discord.ext import commands
import os


###### CONSTANTS        ##########################################################
file_extensions = ['.jpg', '.png', '.gif']                                                                              # The image file extensions supported
TOKEN_FILE = '.emote_dealer.token'                                                                                      # Name of the text file storing the unique Discord bot token (very dangerous, do not share)

# Gets the Discord bot token
def get_token(token_file):
    with open(token_file, 'r') as f:
        return f.read()


###### DISCORD STUFF ############################################################
### Creating the bot!
bot = commands.Bot(command_prefix='emote ')


### EVENTS ###
# Runs this when the bot becomes online
@bot.event
async def on_ready():
    print("Ready to deal some emotes! B)")
    print(bot.user.name)
    await bot.change_presence(activity=discord.Game('with your emotions 😎'))                                           # custom status! (has a new syntax)



### THIS MAKES THE BOT REACT TO MESSAGES WITHOUT THE PREFIX
@bot.event
async def on_message(message):   
    text = message.content.split()

    # Handles errors when there's no text
    try:
        emote = text[0]
    except IndexError:
        emote = "IndexError"

    # Only one-word commands are registered
    if len(text) > 1: return

    # Dealing the emote
    await DealEmote(message, emote)


### Actually gets the emote file and uploads it
async def DealEmote(message, emote):
    for ext in file_extensions:                                                                                             # Checks if the keyword exists on disk as an emote with any of the file types available
        filename = f'{emote}{ext}'
        
        if os.path.isfile(filename):
            print("### Dealt a " + emote)
            await message.channel.send(file=discord.File(filename))
    






###### RUNNING THE BOT #################################################
if __name__ == "__main__":
    TOKEN = get_token(TOKEN_FILE)
    print("_____________EmoteDealer INITIALISED_____________")
    bot.run(TOKEN)



