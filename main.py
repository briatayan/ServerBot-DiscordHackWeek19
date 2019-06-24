import discord

# bot token constant
TOKEN = 'NTkyNzczNTg2NzE3MjQ1NDQx.XRENsA.4_7Ft1ZD7n3Ck6QG0kjpe5_uy1g'

client = discord.Client()

# responds to !hello command
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

# initial code
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
