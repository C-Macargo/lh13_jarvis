import discord
from discord.ext import commands
from youtube_streamer import YouTubeStreamer
import imageio_ffmpeg as ffmpeg

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='play')
    async def play(self, ctx, *, url: str):
        if not ctx.author.voice:
            await ctx.send("You need to be in a voice channel to use this command.")
            return

        audio_url = YouTubeStreamer.get_audio_url(url)
        if not audio_url:
            await ctx.send("Could not extract audio from the provided URL.")
            return

        channel = ctx.author.voice.channel
        voice_client = await channel.connect()

        ffmpeg_executable = ffmpeg.get_ffmpeg_exe()

        ffmpeg_options = {
            'options': '-vn',
            'executable': ffmpeg_executable,
        }
        audio_source = discord.FFmpegPCMAudio(audio_url, **ffmpeg_options)

        voice_client.play(audio_source, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send("Now playing audio.")

    @commands.command(name='leave')
    async def leave(self, ctx):
        for vc in self.bot.voice_clients:
            if vc.guild == ctx.guild:
                await vc.disconnect()

def setup(bot):
    bot.add_cog(MusicCog(bot))
