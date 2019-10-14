import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def on_member_join(self, member):
        print(f'{member} has joined a server.')

    async def on_member_remove(self, member):
        print(f'{member} has left a server.')

    async def on_message_delete(self, message):
        await message.channel.send('A message was deleted here')

    async def on_message(self, message):
        if message.author == bot.user:
            return

        user = message.author.name
        msg = message.content
        print(f'{user} said {msg}')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("Invalid command used.")
        if isinstance(error, commands.CommandsNotFound):
            await ctx.send("Please pass in all required arguments.")

        raise error

def setup(bot):
    bot.add_cog(Events(bot))
