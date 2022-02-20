from discord.ext import commands
from os import getenv
import traceback
import re

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def niku(ctx, arg):
    re_arg = arg.replace("MIKUEC", "NIKUEC").replace("mikuec", "nikuec").replace("みくえっく", "にくえっく").replace(
        "ライブ", "焼き肉").replace("ステージ", "プレート").replace("楽曲", "お肉").replace("曲目", "皿目").replace("曲", "肉")
    await ctx.send(re_arg)


@bot.event
async def on_message(message):
    s = re.search(r'MIKUEC|mikuec|みくえっく|ライブ|ステージ|曲', message.content)
    if (s is not None):
        nikurep = message.content.replace("MIKUEC", "NIKUEC").replace("mikuec", "nikuec").replace("みくえっく", "にくえっく").replace(
            "ライブ", "焼き肉").replace("ステージ", "プレート").replace("楽曲", "お肉").replace("曲目", "皿目").replace("曲", "肉")
        await message.reply(nikurep)


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
