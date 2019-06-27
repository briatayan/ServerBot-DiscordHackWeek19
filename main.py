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
    msg = ctx.message.content.strip("!addserver")
    name = ctx.message.content.split(":",2)[0].split(",")
    tags = ctx.message.content.split(":",2)[1].split(",")
    description = ctx.message.content.split(":",2)[2].split(",")
    if len(tags) >= 1 and len(tags) <= 10:
        try:
            print(helperMethods.tagsplit(msg, ":"))
            serverMethods.serverAdd(name,tags,description)
            await ctx.send(confmessage)

        except TypeError:
            await ctx.send(missmessage)

        except:
            await ctx.send(rejmessage)


client.run(TOKEN)
