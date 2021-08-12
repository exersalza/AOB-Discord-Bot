import os
import discord

from config import DISCORD_TOKEN as TOKEN
from config import PREFIX
from discord.ext import commands

## INTENT CONTROL ##
intents = discord.Intents.all()

# User Definition -> Bot / self.bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents,
                   help_command=None, description="Created by exersalza")


# Cog Loader
for filename in os.listdir("cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f"cogs.{filename[:-3]}")


bot.run(TOKEN)
