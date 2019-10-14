import discord
from discord.ext import commands
import json
import os
import random
import asyncio
from itertools import cycle
import giphy_client
from discord.ext.commands import Bot
from giphy_client.rest import ApiException

TOKEN = 'token'
giphy_token = 'token'

def get_prefix(bot, message):
    with open('Tsukuyomi Bot - Copy/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

#Prefix log
bot = commands.Bot(command_prefix = get_prefix)
api_instance = giphy_client.DefaultApi()

async def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(giphy_token, query, limit=3, rating='g')
        lst = list(response.data)
        gif = random.choices(lst)

        return gif[0].url

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

bot.remove_command('help')

@bot.event
async def on_guild_join(guild):
    with open('Tsukuyomi Bot - Copy/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('Tsukuyomi Bot - Copy/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
@bot.event
async def on_guild_remove(guild):
    with open('Tsukuyomi Bot - Copy/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('Tsukuyomi Bot - Copy/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
@bot.command()
async def changeprefix(ctx, prefix):
    with open('Tsukuyomi Bot - Copy/prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('Tsukuyomi Bot - Copy/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

#EVENTS
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print('--------')

#Load Cogs
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    ctx.send(f'{cog} got loaded')

#Unload Cogs
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    ctx.send(f'{cog} got unloaded')

#Reload Cogs
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    ctx.send(f'{cog} got reloaded')


#Cogs File
for filename in os.listdir('Tsukuyomi Bot - Copy/cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#COMMANDS
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')
@bot.command()
async def echo(ctx, *, words: commands.clean_content):
    await ctx.send(words)
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member

    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.colour.purple(), timestamp=ctx.message.created_at)

    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Request by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name='ID:', value=member.id)
    embed.add_field(name='Guild name:', value=member.display_name)

    embed.add_field(name='Created at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    embed.add_field(name='Joined at:', value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))

    embed.add_field(name=f'Roles ({len(roles)})', value=' '.join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)

    embed.add_field(name='Bot?', value=member.bot)

    await ctx.send(embed=embed)
@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Tsukuyomi Bot", description="Nicest bot there is ever.", colour=discord.Colour.purple())

    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
    # give info about you here
    embed.add_field(name="Author", value="Amaterasu")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite this bot to their server
    embed.add_field(name="Invite Bot", value="[Invite link](https://discordapp.com/api/oauth2/authorize?bot_id=631932915491536942&permissions=8&scope=bot)")

    await ctx.send(embed=embed)
@bot.command()
async def rban(ctx, member : discord.Member):
    await ctx.send(f'{member} has lost rights to be a person')

#EMBEDS
@bot.command()
async def gif(ctx):
    embed = discord.Embed(title='', description='', colour=discord.Colour.purple())

    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.set_image(url='https://media.giphy.com/media/143v0Z4767T15e/giphy.gif')

    await ctx.send(embed=embed)


#BACKGROUND TASKS
async def chag_pr():
    await bot.wait_until_ready()

    statuses = ['with your heart <3', 'Bot 101 course', 'How to get away with murder', 'Clap and seek', '.help', 'Having fun', 'Being a good bot', 'How to become Human', 'Eating food like people', 'Watching Anime', 'How to be a waifu']

    while not bot.is_closed():
        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(status))

        await asyncio.sleep(30)

#help
@bot.command(aliases=['help'])
async def commands(ctx):
    embed = discord.Embed(title="Tsukuyomi Bot", description="List of commands are:", colour=discord.Colour.purple())

    embed.add_field(name="__`add X Y`__", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="__`multiply X Y`__", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="__`greet`__", value="Gives a nice greet message", inline=False)
    embed.add_field(name="__`cat`__", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="__`dadjoke`__", value="Gives a dad joke making everyone cringe.", inline=False)
    embed.add_field(name="__`info`__", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="__`help`__", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def bite(ctx, member: discord.Member):
    await ctx.send('{0.name} bites {member.name}')

bot.loop.create_task(chag_pr())
bot.run(TOKEN)
