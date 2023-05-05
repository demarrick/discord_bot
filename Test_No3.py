import discord 
from discord.ext import commands
from discord.utils import get
from asyncio import sleep
from playsound import playsound
intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    channel=bot.get_channel(1095104835814166724)
    await channel.send(f'Ciaoo! Io sono {bot.user.name}.')# ({bot.user.id}).')



#@bot.event
#async def on_disconnect():
#    channel = bot.get_channel(1095104835814166724)  
#    await channel.send("Bot has gone offline.")
#@bot.event
#async def on_voice_state_update(member, before, after):
#    if before.channel is None and after.channel is not None:
#        channel = bot.get_channel(1095104835814166724)
#        await channel.send(f"Buon viaggio, {member.display_name}!")
#        playsound('/Users/riccardodemarco/Desktop/Test_No1/Sample.m4a')


@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        channel = bot.get_channel(1095104835814166724)
        if member.name != 'Test_No1' :
         await channel.send(f"Buon viaggio, {member.display_name}!")    

bot.run('MTEwMjE4NzMwMTYwNzU4MzgwNA.GCgrTX.jCZV5u2AQ0ewl3UPQgIWqhTi_AdPk982G0Zvs8')
