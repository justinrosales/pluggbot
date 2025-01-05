import discord
from discord.ext import commands
import os

from help_cog import help_cog
from music_cog import music_cog

from dotenv import load_dotenv

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Remove the default help command
bot.remove_command("help")

# Define the setup hook for asynchronous initialization
async def setup():
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(music_cog(bot))

# Override the setup_hook method to call setup when the bot starts
bot.setup_hook = setup

load_dotenv()
bot.run(os.getenv("TOKEN"))
