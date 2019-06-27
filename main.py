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
    #if the message has a name, tags, and a description, then check and make sure they're the admin/owner than print the message
    confmessage = "Great! Your server is under review and will be apart of the server list soon."
    #else reject it.
    rejmessage = "Oh no! It looks like something went wrong. Don't forget the format is name : tag, tag, tag : description"
    #else, say it has not been added and tell them to add an id, tags, and a description.
    msg = ctx.message.content.strip("!addserver")
    tags = ctx.message.content.split(":",2)[1].split(",")

    if len(tags) >= 1 and len(tags) <= 10:
        print(helperMethods.tagsplit(msg, ":"))
        await ctx.send(confmessage)

    else
        awai ctx.send(rejmessage)


client.run(TOKEN)
