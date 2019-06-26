import discord
from discord.ext import commands
import auth
import logging
import helperMethods
import AddToServerList

logging.basicConfig(level=logging.INFO)

TOKEN = auth.TOKEN

#client = discord.Client()

client= commands.Bot(command_prefix='!')

client.remove_command('help')

db = dict(dict())

# responds to commands
@client.event

#commands go here

async def on_ready():
    print("bot is ready")

@client.event
async def on_memeber_join(memeber):
    print ("f'{memeber} has joined serve.")

@client.event
async def on_memeber_remove(memeber):
    print ("f'{memeber} has left the serve.")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong!{round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    msg = "List of commands go here"
    await ctx.send(msg)

@client.command()
async def Hello(ctx):
    await ctx.send(f"hello {ctx.author.mention}!")

@client.command()
async def addserver(ctx)
    #if the author's message contains a server id, tags, and a description then send a message saying it has been added

    await ctx.()
    #else, say it has not been added and tell them to add an id, tags, and a description.
return

client.run(TOKEN)
