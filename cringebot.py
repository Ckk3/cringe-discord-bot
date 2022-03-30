import os
import discord

#Instance to connect to discord
client = discord.Client()

#Getting users ID from env variables
ckk = os.getenv('ckkDISC_ID')
discodia = os.getenv('discordiaDISC_ID')
heleven = os.getenv('helevenDISC_ID')
theus = os.getenv('theusDISC_ID')
rdgnow = os.getenv('rdgnowDISC_ID')
murilo = os.getenv('muriloDISC_ID')
markoz = os.getenv('markozDISC_ID')
maico = os.getenv('maicoDISC_ID')
jener = os.getenv('jenerDISC_ID')

#Dict with the reactions to users
reactions = {
    ckk:['ℹ️','🇳','🇨','🇪','🇱','™️'],
    discodia:['🇧','🇦','🇸','🇪','🇩'],
    heleven:['🇧','🇷','🇴','🇽','🇦','⤵️'],
    theus:['🇱','🇴','🇻','🇪','🇷','❤️'],
    rdgnow:['🇨','🇷','ℹ️','🇳','🇬','🇪'],
    murilo:['🇹','🇨','🇭','🇴','🇱','🇦'],
    markoz:['🇱','🇪','ℹ️','🇹','3️⃣','🇷','🇴','🥛'],
    maico:['🇨','🇺','🇬','🇷','🇦','🇹','ℹ️','🇸','😋'],
    jener:['🆓','🇫','ℹ️','🇷','🇪','👶']
}

@client.event
async def on_ready():
    print('Ta rodando como -> {0.user}'.format(client))

@client.event
async def on_message(message):
    authorID = str(message.author.id)

    if authorID in reactions:
        for emoji in reactions[authorID]:
            await message.add_reaction(emoji)
        
client.run(os.getenv('discordAPI_KEY'))


