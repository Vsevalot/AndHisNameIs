import discord
from settings import BOT_TOKEN


client = discord.Client()

def is_command(message: discord.message) -> bool:
  if message.content.startswith('$'):
    return True
  return False

async def process_command(command: discord.message):
  if command.content.startswith('$hello'):
    await command.channel.send("Hello!")


@client.event
async def on_ready() -> None:
  print(f'Logged as {client.user}')


@client.event
async def on_message(message: discord.message) -> None:
  print(f"message type is: {type(message)}")
  if message.author == client.user:
    return

  if is_command(message):
    await process_command(message)

if __name__ == "__main__":
  client.run(BOT_TOKEN)
