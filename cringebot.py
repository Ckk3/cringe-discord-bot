import os
from unicodedata import name
import discord

#Instance to connect to discord
client = discord.Client()

ckkID = os.getenv('ckkDISC_ID')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.author.id) == ckkID:
        await message.add_reaction('🇧')
        

client.run(os.getenv('discordAPI_KEY'))


