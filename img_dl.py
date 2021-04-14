# Downloads images and gifs for the emote dealer to deal

###### THE IMPORTS      ##########################################################
import discord
from discord.ext import commands
import os
import urllib.request

# The image file extensions supported
file_extensions = ['.jpg', '.png', '.gif']

###### HELPER FUNCTIONS ###########################################################
def dl_img(url, name):
    file_ext = url[-4:]                                 # gets the last 4 characters in the url (.gif, .png, .jpg hopefully)
    if (not file_ext in file_extensions):               # checks if the url's extension is valid
        print(f'INVALID FILE EXTENSION: {url}')
        return
    
    file_name = name + file_ext                         # combines the desired name with the matching file type

    urllib.request.urlretrieve(url, file_name)          # actually downloads the image

    print(f'Downloaded image from: {url}')
    print(f'Saved image as: {file_name}')



print("_____________EmoteAgent INITIALISED_____________")

###### DISCORD STUFF ############################################################
### Creating the bot!
bot = commands.Bot(command_prefix='emote ')

###### EVENTS        ##########################################################
# Runs this when the bot becomes online
@bot.event
async def on_ready():
    print("Ready to add some emotes!")
    print(bot.user.name)
    #The Bot's status/game he is playing
    await bot.change_presence(activity=discord.Game('Call me'))   # custom status! (has a new syntax)



###### COMMANDS ############################################################
@bot.command()
async def add(ctx, arg1, arg2):
    file_name = arg1
    url = arg2

    # calls the helper to download the emote
    dl_img(url, file_name)

    #Embed
    embed = discord.Embed(title="Added a new emote!", description=arg1, color=0xDD2F2F)
    embed.set_image(url = arg2)
    embed.set_thumbnail(url="https://i.imgur.com/SpVKNOf.png")
    await ctx.send(embed=embed)




#Runs the bot on the specified token
bot.run("NjExOTI3Nzk4MzAyNjM4MTE0.XVa8nQ.NFHSHQLQRxzTwBnKwqjevpMzRFU")
