import discord
from discord.ext import commands
import os, asyncio
from music_cog import MusicCog  
from help_cog import HelpCog
from purge_cog import PurgeCog

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), case_insensitive=True)
bot.remove_command('help')

async def main():
    print("LH13_jarvis is online")
    async with bot:
        await bot.add_cog(HelpCog(bot))
        await bot.add_cog(MusicCog(bot))
        await bot.add_cog(PurgeCog(bot))
        await bot.start(os.getenv('DISCORD_TOKEN'))

asyncio.run(main())
