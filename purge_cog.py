import discord
from discord.ext import commands

class PurgeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='purge', help='Deletes the last 10 messages from chat')
    @commands.has_permissions(manage_messages=True) 
    @commands.has_role("Secretário do partido")

    async def purge(self, ctx):
        if ctx.channel.permissions_for(ctx.guild.me).manage_messages:
            deleted = await ctx.channel.purge(limit=10)
            embed = discord.Embed(title='Purge complete', description=f'{len(deleted)} messages have been deleted.', color=0xFFFF00)
            confirmation_message = await ctx.send(embed=embed)

            await confirmation_message.delete(delay=15)  
        else:
            await ctx.send("I do not have permissions to manage messages in this channel.")
