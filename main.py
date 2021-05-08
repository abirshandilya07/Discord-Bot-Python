import discord, os, requests, json
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello! Tip: you can get some help by $help command')
  
  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$help'):
    await message.channel.send('Hey Buddies! I am a new bot which can be used for sending inspirational messages with the command $inspire')

keep_alive()
client.run(os.getenv('TOKEN'))