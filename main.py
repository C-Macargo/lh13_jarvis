import discord
from discord.ext import commands
import os, asyncio
from music_cog import MusicCog  

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

async def main():
    async with bot:
        await bot.add_cog(MusicCog(bot))  
        await bot.start(os.getenv('DISCORD_TOKEN'))  
asyncio.run(main())
