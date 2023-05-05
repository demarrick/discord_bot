import discord



token='MTEwMjE4NzMwMTYwNzU4MzgwNA.GCgrTX.jCZV5u2AQ0ewl3UPQgIWqhTi_AdPk982G0Zvs8'

intents = discord.Intents.default()
intents.members = True 
intents.messages=True
intents.message_content=True
intents.voice_states=True
client= discord.Client(intents=intents)

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
          elif '/come stai?' in message.content:
              print(f'Bene {message.author.name} grazie! Tu?')
              channel=client.get_channel(1095104835814166724)
              await channel.send(f'Bene {message.author.name}, grazie! Tu?')

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        channel = client.get_channel(1095104835814166724)
        if member.name != client.user.name :
         print(f'Buon divertimento, {member.display_name}!')
         await channel.send(f"Buon divertimento, {member.display_name}!")
         
              
client.run(token)