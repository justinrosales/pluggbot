import discord
from discord.ext import commands
from yt_dlp import YoutubeDL
import os
import asyncio

os.environ["FFMPEG_BINARY"] = "ffmpeg"

class music_cog(commands.Cog):
    def __init__(self, bot):

        self.bot = bot
        self.is_playing = False
        self.is_paused = False
        self.music_queue = []

        # Options for yt-dlp to extract audio
        self.YDL_OPTIONS = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'extract_flat': False,
            'quiet': True,
            'default_search': 'auto',
        }
        self.FFMPEG_OPTIONS = {'options': '-vn'}
        self.BEFORE_OPTIONS = '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'

        self.vc = None

    # Search for a song on YouTube or SoundCloud
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                if "soundcloud.com" in item:
                    info = ydl.extract_info(item, download=False)
                else:
                    info = ydl.extract_info(f"ytsearch:{item}", download=False)['entries'][0]
            except Exception as e:
                print(f"Error: {e}")
                return False
            
        return {'source': info['url'], 'title': info['title']}

    # Play the next song in the queue
    async def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']
            self.music_queue.pop(0)
            self.vc.play(
                discord.FFmpegPCMAudio(m_url, before_options=self.BEFORE_OPTIONS, options=self.FFMPEG_OPTIONS['options']),
                after=lambda e: self.bot.loop.create_task(self.play_next())
            )
        else:
            self.is_playing = False

    # Start playing music from the queue (infinite loop checking) 
    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True
            m_url = self.music_queue[0][0]['source']

            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                if self.vc == None:
                    await ctx.send("Could not connect to a voice channel.")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])

            self.music_queue.pop(0)
            self.vc.play(
                discord.FFmpegPCMAudio(m_url, before_options=self.BEFORE_OPTIONS, options=self.FFMPEG_OPTIONS['options']),
                after=lambda e: self.bot.loop.create_task(self.play_next())
            )    
        else:
            self.is_playing = False

    # Command to play or queue a song
    @commands.command(name="play", aliases=["p"], help="Plays a selected song from youtube")
    async def play(self, ctx, *args):
        query = " ".join(args)

        try:
            voice_channel = ctx.author.voice.channel
        except:
            await ctx.send("You need to connect to a voice channel.")
            return
         
        if self.is_paused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download song. Use a different keyword and try again. This could be due to playlist or a livestream format.")
            else:
                if self.is_playing:
                    await ctx.send(f"**#{len(self.music_queue)+2} -'{song['title']}'** added to the queue")  
                else:
                    await ctx.send(f"**'{song['title']}'** added to the queue")  
                self.music_queue.append([song, voice_channel])
                if self.is_playing == False:
                    await self.play_music(ctx)

    # Command to stop and disconnect the bot
    @commands.command(name="stop", help="Kick the bot from VC")
    async def dc(self, ctx):
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()

    # Commands to pause or resume the current song
    @commands.command(name="pause", help="Pauses the current song being played")
    async def pause(self, ctx, *args):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()
        elif self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
    @commands.command(name = "resume", help="Resumes playing with the discord bot")
    async def resume(self, ctx, *args):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()

    # Command to display the queue
    @commands.command(name="queue", aliases=["q"], help="Displays the current songs in queue")
    async def queue(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += f"#{i+1} -" + self.music_queue[i][0]['title'] + "\n"

        if retval != "":
            await ctx.send(f"queue:\n{retval}")
        else:
            await ctx.send("Music queue is empty.")
    
    # Command to skip the current song
    @commands.command(name="skip", aliases=["s"], help="Skips the current song being played")
    async def skip(self, ctx):
        if self.vc != None and self.vc:
            self.vc.stop()
            await self.play_music(ctx)

    # Command to clear the queue
    @commands.command(name="clear", aliases=["c"], help="Stops the music and clears the queue")
    async def clear(self, ctx):
        if self.vc != None and self.is_playing:
            self.vc.stop()
        self.music_queue = []
        await ctx.send("Music queue cleared.")
