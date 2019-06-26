import discord
import logging

import auth
import helperMethods
import AddToServerList

logging.basicConfig(level=logging.INFO)

TOKEN = auth.TOKEN

client = discord.Client()

db = dict(dict())

# responds to commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!help'):
        msg = ":question: List of ServerBot Commands :question:\n- !search : " +\
                "Enter a list of tags to search for a server! ex. !search FFXIV Adult Siren"
        msg = msg.format(message)
        await client.send_message(message.channel, msg)

# initial code
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
