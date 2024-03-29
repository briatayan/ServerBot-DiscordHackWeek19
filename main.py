import discord
from discord.ext import commands
import logging
import auth
import helperMethods
import serverMethods

logging.basicConfig(level=logging.INFO)

TOKEN = auth.TOKEN

client= commands.Bot(command_prefix='!')

client.remove_command('help')

# initial code

@client.event

#commands go here
async def on_ready():
    print("bot is ready")

@client.command()
async def help(ctx):
    msg = "Need some help? Here are the commands and how to use them! \n\
!addserver allows you to add yourserver to our running list. Use: !addserver tag1, tag2, etc. up to tag10; a description; and the invite link \n\
!editserver allowes you to edit your tags and description. Use: !editserver tag; tag1, tag2, etc. up to tag10; description; this is a description. or \n\
!deleteserver deletes your server from the list. Use: !deleteserver \n\
!serversearch allows you to search for servers you have tags in common with. Use !serversearch tag1, tag2, etc. up to tag10. \n\
!help well this is awkward."
    await ctx.send(msg)

@client.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}!")

@client.command()
async def addserver(ctx):
    confmessage = "Great! Your server is under review and will be apart of the server list soon."
    rejmessage = "Oh no! It looks like something went wrong. Don't forget the format is name ; tag, tag, tag ; description"
    missmessage = "Looks like you're missing either a name, 1-10 tag(s), or a description."
    servadmin = "It looks like you are neither server owner or administrator!"
    msg = ctx.message.content.strip("!addserver")
    id = ctx.guild.id
    name = ctx.guild.name
    # This is the old name command name = ctx.message.content.strip("!addserver").split(":",2)[0].split(",")
    tags = msg.strip().split(";")[0].strip()
    # old tag command description = ctx.message.content.split(":",2)[1].split(",")
    description = msg.split(";",2)[1].strip()
    invite = msg.split(";",3)[2].strip()
    if ctx.message.author.guild_permissions.administrator:

        len(tags) >= 1 and len(tags) <= 10
        try:
            print(helperMethods.tagsplit(msg, ";"))
            serverMethods.serverAdd(str(id),name,tags,description,invite)
            await ctx.send(confmessage)

        except TypeError:
            await ctx.send(missmessage)

        except:
            await ctx.send(rejmessage)
    else:
        await ctx.send(servadmin)
    return

@client.command()
async def deleteserver(ctx):
    confmessage = "Great! Your server you will be removed from the list shorly."
    rejmessage = "Oh no! It looks like something went wrong."
    missmessage = "It looks like you're missing something!"
    servadmin = "It looks like you are not a server owner or administrator. oops"
    msg = ctx.message.content.strip("!deleteserver")
    id = ctx.guild.id

    if ctx.message.author.guild_permissions.administrator:
        try:
            print(id)
            serverMethods.serverRemove(str(id))
            await ctx.send(confmessage)

        except TypeError:
            await ctx.send(missmessage)

        except:
            await ctx.send(rejmessage)
    else:
        await ctx.send(servadmin)

@client.command()
async def editserver(ctx):
    confmessage = "Great! Your server has been edited!"
    rejmessage = "Oh no! It looks like your server wasn't edited"
    missmessage = "Looks like you're missing a new tag or Description! Use !editserver tags; tag 1, tag 2, tag 3. description; description goes here. or invite; new link here"
    servadmin = "It looks like you are neither server owner or administrator! Try asking one of them?"
    msg = ctx.message.content.replace("!editserver", "")
    id = ctx.guild.id
    tags = msg.split(";")[0].strip()
    description = msg.split(";")[1].strip()
    tags = tags.lower()
    if ctx.message.author.guild_permissions.administrator:
        ctx.message.content
        len(tags) >= 1 and len(tags) <= 10
        try:
            serverMethods.serverEdit(str(id), tags, description)
            await ctx.send(confmessage)

        except TypeError:
            await ctx.send(missmessage)

        except:
            await ctx.send(rejmessage)
    else:
        await ctx.send(servadmin)

@client.command()
async def serversearch(ctx):
    tags = ctx.message.content.strip("!serverSearch")
    result = serverMethods.serverSearch(str(tags))
    if result:
        message = helperMethods.formatMessage(result)
    else:
        message = "There aren't any servers with any of those tags, sorry!"
    await ctx.send(message)

client.run(TOKEN)
