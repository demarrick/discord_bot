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
    if message.content == 'moseca':
        if message.author.voice:
            channel = message.author.voice.channel
            voice_client = await channel.connect()
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('/Users/riccardodemarco/Desktop/Test_No1/Sample.m4a'))
            voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
        else:
            await message.channel.send("You must be in a voice channel to play music.")
    elif message.content == 'stop':
        for vc in bot.voice_clients:
            if vc.guild == message.guild:
                vc.stop()
    elif message.content == 'Archesso è un?':
        print('GAY')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        channel = bot.get_channel(1095104835814166724)
        await channel.send(f"Buon viaggio, {member.display_name}!")

bot.run('MTEwMjE4NzMwMTYwNzU4MzgwNA.GCgrTX.jCZV5u2AQ0ewl3UPQgIWqhTi_AdPk982G0Zvs8')
