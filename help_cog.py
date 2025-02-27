import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  
        
        self.help_message = f"""
**{self.bot.command_prefix}help** - displays all the available commands
**{self.bot.command_prefix}play <keywords>** - finds the song on youtube and plays it in your current channel
**{self.bot.command_prefix}queue (q)** - displays the current music queue
**{self.bot.command_prefix}skip** - skips the current song being played
**{self.bot.command_prefix}clear** - stops the music and clears the queue
**{self.bot.command_prefix}stop** - disconnects the bot from the voice channel
**{self.bot.command_prefix}pause** - pauses the current song being played or resumes if already paused
**{self.bot.command_prefix}resume** - resumes playing the current song
"""

    @commands.command(name="help", help="Displays all avail commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)
