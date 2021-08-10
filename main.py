import os
import discord

from config import DISCORD_TOKEN as TOKEN
from config import PREFIX
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza")


for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")

# bot.load_extension('help')
bot.run(TOKEN)
