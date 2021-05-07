# Downloads images and gifs for the emote dealer to deal
# NEW !! - Updated to use Slash Commands /// WOW!!

###### THE IMPORTS      ##########################################################
import discord                                          # the main discord module
from discord.ext import commands                        # commands are nice
import urllib.request                                   # use to download images from the interwebz
import os

# The Slash Commands module - NEW NEW NEW !!
from discord_slash import SlashCommand, SlashContext                                                                    # used to create slash commands /
from discord_slash.utils.manage_commands import create_option                                                           # used to specify the type of argument required

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



###### SLASH COMMANDS //// #################################################
slash = SlashCommand(bot, sync_commands=True)                                                                           # Initialises the @slash dectorator - NEEDS THE SYNC COMMANDS to be true
guild_ids = [349267379991347200]                                                                                        # The Server ID - not sure why did this needed


# Adds an emote
@slash.slash(name='add',                                                                                                # Name of the Slash command / not the function itself
            guild_ids=guild_ids,                                                                                        # For some reason, this is needed here, but not on the test command?
            description='Adds an emote to Emote Dealer',                                                                # The command's description in the discord UI
            options=[                                                                                                   # First time trying multiple options, let's gooo
                create_option(
                 name="name",                                                                                           # MUST HAVE the SAME NAME as the argument in the function <- actually READ this after copy-pasting !!!
                 description="link the to the image",
                 option_type=3,                                                                                         # 3 = String
                 required=True
               ),
               create_option(
                 name="url",                                                                                            # MUST HAVE the SAME NAME as the argument in the function
                 description="link the to the image",
                 option_type=3,                                                                                         # 3 = String
                 required=True
               )
            ])
async def _add(ctx, name, url):
    # calls the helper to download the emote
    dl_img(url, name)

    #Embed
    embed = discord.Embed(title="Added a new emote!", description=name, color=0xDD2F2F)
    embed.set_image(url = url)
    embed.set_thumbnail(url="https://i.imgur.com/SpVKNOf.png")

    await ctx.send(embed=embed)


# Lists all emotes available
@slash.slash(name="list",
             description="Lists all available emotes 😃",
             guild_ids=guild_ids)
async def _list(ctx):
    files = os.listdir()                                                                                                # gets all files in current directory

    for file in files:
        if file.endswith('.py'):                                                                                        # filters out the python scripts
            files.remove(file)
        
    files = [x[:-4] for x in files]                                                                                     # gets a new list where each list value has the file extension deleted, all in one line of code!
    emotes = ', '.join(files)                                                                                           # joins the array items into a single, comma seperated string

    await ctx.send(f'```{emotes}```')                                                                                   # sends the emote list with monospaced font



###### RUNNING THE BOT #################################################
#Runs the bot on the specified token
bot.run("NjExOTI3Nzk4MzAyNjM4MTE0.XVa8nQ.NFHSHQLQRxzTwBnKwqjevpMzRFU")
