import discord
from discord.ext import commands
import logging
import auth
import helperMethods
import serverMethods

logging.basicConfig(level=logging.INFO)

TOKEN = auth.TOKEN

client= commands.Bot(command_prefix='!')

message = client.get_channel(id)

client.remove_command('help')

# initial code

@client.event

#commands go here
async def on_ready():
    print("bot is ready")

@client.event
async def on_memeber_join(member):
    print ("f'{member} has joined server.")

@client.event
async def on_memeber_remove(member):
    print ("f'{member} has left the server.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!{round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    msg = "List of commands go here"
    await ctx.send(msg)

@client.command()
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}!")

@client.command()
async def addserver(ctx):
    confmessage = "Great! Your server is under review and will be apart of the server list soon."
    rejmessage = "Oh no! It looks like something went wrong. Don't forget the format is name : tag, tag, tag : description"
    missmessage = "Looks like you're missing either a name, 1-10 tag(s), or a description."
    servadmin = "It looks like you are neither server owner or administrator!"
    msg = ctx.message.content.strip("!addserver")
    id = ctx.guild.id
    name = ctx.guild.name
    # This is the old name command name = ctx.message.content.strip("!addserver").split(":",2)[0].split(",")#.helperMethods.tagsplit()
    tags = ctx.message.content.strip("!addserver").replace(" ","").split(",")#.helperMethods.tagsplit()
    # old tag command description = ctx.message.content.split(":",2)[1].split(",")#.helperMethods.tagsplit()
    description = ctx.guild.description
    # This is the old description command description = ctx.message.content.split(":",2)[2].split(",")#.helperMethods.tagsplit()
#replace the colon with a . and remove the # to allow administrator only mode.
    if ctx.message.author.guild_permissions.administrator:

        len(tags) >= 1 and len(tags) <= 10
        try:
            print(helperMethods.tagsplit(msg, ":"))
            serverMethods.serverAdd(str(id),name,tags,description)
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
    missmessage = "Looks like you're missing a new tag or Description! Use !editserver tags: tag 1, tag 2, tag 3, or description: description goes here"
    servadmin = "It looks like you are neither server owner or administrator! Try asking one of them?"
    msg = ctx.message.content.strip("!editserver")
    id = ctx.guild.id
    tags = ctx.message.content.strip("!editserver").split(":")[0]
    description = ctx.guild.description
    if ctx.message.author.guild_permissions.administrator:
        ctx.message.content
        len(tags) >= 1 and len(tags) <= 10
        try:
            print(tags)
            print(helperMethods.tagsplit(msg, ":"))
            serverMethods.serverEdit(str(id), tags, description)
            await ctx.send(confmessage)

        except TypeError:
            await ctx.send(missmessage)

        except:
            await ctx.send(rejmessage)
    else:
        await ctx.send(servadmin)
client.run(TOKEN)
