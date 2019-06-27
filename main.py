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

<<<<<<< HEAD
# initial code

=======
# responds to commands
>>>>>>> ce2110a69c49a20069dc8b60b4a831fc552fee03
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
async def addserver(ctx)
    await 
    #if the author's message contains a server id, tags, and a description then send a message saying it has been added

    await ctx.()
    #else, say it has not been added and tell them to add an id, tags, and a description.
return

client.run(TOKEN)
