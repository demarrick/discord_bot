import discord 
from playsound import playsound
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
   if message.content == 'moseca' :
      global audio
      audio=playsound('/Users/riccardodemarco/Desktop/Test_No1/Sample.m4a')
   elif message.content == 'stop' :
      audio.stop()
   elif message.content == 'Archesso è un?' :
      print('GAY')

async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        channel = bot.get_channel(1095104835814166724)  
        await channel.send(f"Buon viaggio, {member.display_name}!")

bot.run('MTEwMjE4NzMwMTYwNzU4MzgwNA.GBqgZp.vUnR6eP4UXv1FG-1n1NE4ArAtsfOjOHZqxV5jg')


