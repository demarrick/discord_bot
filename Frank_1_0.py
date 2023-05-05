import discord
from playsound import playsound
import matplotlib.pyplot as plt
import pandas as pd
import yfinance
from pandas_datareader import data as pdr
yfinance.pdr_override()
from datetime import date, timedelta
import seaborn as sns
from discord import FFmpegPCMAudio
import youtube_dl
import ctypes.util
import asyncio

token='MTEwMjE4NzMwMTYwNzU4MzgwNA.GSdFIR.d-EIi2R3Ws9I9yzqOsUjSoQ2xLwUZ2B1h3iH40'

libopus_path='/opt/homebrew/lib/libopus.dylib'
discord.opus.load_opus(libopus_path)
intents = discord.Intents.default()
intents.members = True 
intents.messages=True
intents.message_content=True
intents.voice_states=True
client= discord.Client(intents=intents)

def AppleStock():
    '''shows apple stock plot'''
    today=date.today()
    df=pdr.get_data_yahoo('AAPL', start='2015-01-01', end=today)
    df_1=df.reset_index()
    sns.set_style('whitegrid')
    sns.relplot(data=df_1, x='Date', y='Adj Close', kind='line')
    plt.savefig('plot.png')

@client.event
async def on_ready():
     print(f"Bot is online and logged in as {client.user}.")
     channel=client.get_channel(1095104835814166724)
     await channel.send(f'Ciaoo! Io sono {client.user.name}.')

@client.event
async def on_message(message):
     if message.author != client.user:
          print(f'Author is not the Bot.')
          if '/ciao' in message.content:
               print(f'Ciao {message.author.name}!.')
               channel=client.get_channel(1095104835814166724)
               await channel.send(f'Ciao {message.author.name}!.')
          elif '/come stai' in message.content:
              print(f'Bene {message.author.name} grazie! Tu?')
              channel=client.get_channel(1095104835814166724)
              await channel.send(f'Bene {message.author.name}, grazie! Tu?')
          elif '/come va apple' in message.content:
              AppleStock()
              channel=client.get_channel(1095104835814166724)
              await channel.send(file=discord.File('plot.png'))
              plt.clf()
          elif '/play' in message.content:
              voice_channel=client.get_channel(1095104835814166725)
              channel=client.get_channel(1095104835814166724)
              if not client.voice_clients:
               vc=await voice_channel.connect()
               await channel.send(f'Mi sto unendo alla chat vocale!')
               vc.play(discord.FFmpegPCMAudio('/Users/riccardodemarco/Desktop/discord_bot/Sample.m4a'), after=lambda e: asyncio.run_coroutine_threadsafe(vc.disconnect(), client.loop))
              else:
                  voice_c=client.voice_clients[0]
                  if voice_c.is_playing()==False: 
                      voice_c.play(discord.FFmpegPCMAudio('/Users/riccardodemarco/Desktop/discord_bot/Sample.m4a'), after=lambda e: asyncio.run_coroutine_threadsafe(voice_c.disconnect(), client.loop))
                  else:
                      await channel.send(f'Sto gia pompando la canzoncina!')
          elif '/disconnettiti' in message.content: 
              if client.voice_clients:
                  channel=client.get_channel(1095104835814166724)
                  await channel.send(f'Certo! :)')
                  voice=client.voice_clients[0]
                  await voice.disconnect()     
              else:
                  channel=client.get_channel(1095104835814166724)
                  await channel.send(f'Non sono connesso alla chat vocale.')
          elif '/stop' in message.content:
              if client.voice_clients:
                  new_voice=client.voice_clients[0]
                  if new_voice.is_playing()==True:
                      new_voice.stop()
                      await new_voice.disconnect()
                  else:
                     channel=client.get_channel(1095104835814166724)
                     await channel.send(f'Non sto riproducendo musica!')
              else:
                 channel=client.get_channel(1095104835814166724)
                 await channel.send(f'Non sono connesso alla chat vocale!')
          elif '/help' in message.content:
              channel=client.get_channel(1095104835814166724)
              await channel.send(f'Premi "/ciao" per salutarmi.')
              await channel.send(f'Premi "/come stai" per sapere come sto.')
              await channel.send(f'premi "/come va apple" per saper il prezzo di chiusura aggiustato dello stock di Apple Silicon, dal 2015 a oggi.')
              await channel.send(f'Premi "/play" per riprodurre la sigla.')
              await channel.send(f'Premi "/stop" per interrompere la riproduzione.')
              await channel.send(f'Premi "/disconnettiti" per farmi uscire dalla chat vocale.')
              await channel.send(f'Premi "/archesso" per ...')
          elif '/archesso' in message.content:
              channel=client.get_channel(1095104835814166724)
              await channel.send(f'GAY')
              
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        channel = client.get_channel(1095104835814166724)
        if member.name != client.user.name :
         print(f'Buon divertimento, {member.display_name}!')
         await channel.send(f"Buon divertimento, {member.display_name}!")
         if not client.voice_clients:
          voice_channel=client.get_channel(1095104835814166725) 
          sound=await voice_channel.connect() 
          source=discord.FFmpegPCMAudio('/Users/riccardodemarco/Desktop/discord_bot/Sample.m4a')
          volume = 0.09
          source=discord.PCMVolumeTransformer(source, volume=volume)
          sound.play(source, after=lambda e: asyncio.run_coroutine_threadsafe(sound.disconnect(), client.loop))

client.run(token)