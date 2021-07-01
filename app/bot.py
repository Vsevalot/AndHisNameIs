import discord


def is_command(message: discord.Message) -> bool:
    if message.content.startswith('$'):
        return True
    return False


class AndHisNameIs(discord.Client):

    async def on_ready(self) -> None:
        print(f'Logged as {self.user}')

    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.user:
            return
        if is_command(message):
            await self.process_command(message)

    async def process_command(self, command: discord.Message):
        if command.content.startswith('$hello'):
            await command.channel.send("Hello!")
