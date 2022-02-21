from discord.ext import commands
from os import getenv
import traceback
import re

bot = commands.Bot(command_prefix='!')


nikulist = [("MIKUEC", "NIKUEC"), ("mikuec", "nikuec"), ("みくえっく", "にくえっく"),
            ("ミクエック", "ニクエック"), ("ライブ", "焼き肉"), ("ステージ", "プレート"),
            ("楽曲", "お肉"), ("曲目", "皿目"), ("曲", "肉"), ("聞こえる", "焼かれる"), ("聞", "焼")]


def nikurep(line):
    newline = line
    for before, after in nikulist:
        newline = newline.replace(before, after)
    return newline


@bot.event
async def on_ready():
    print('Done Login')


@bot.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.listen()
async def on_message(message):
    if message.author.bot:
        return
    if re.match(r'!', message.content):
        return
    sniku = re.search(r'MIKUEC|mikuec|みくえっく|ライブ|ステージ|曲', message.content)
    if (sniku is not None):
        re_mess = nikurep(message.content)
        await message.reply(re_mess)
        await bot.process_commands(message)


@bot.command(name="niku")
async def niku(ctx, arg):
    if ctx.author.bot:
        return
    re_arg = nikurep(arg)
    await ctx.send(re_arg)


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
