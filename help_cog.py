import discord
from discord.ext import commands

class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        embed = discord.Embed(title="help", description="List of available commands:", color=0x00ff00)
        for command in self.bot.commands:
            if command.name == "help":
                continue
            embed.add_field(name=f"{self.bot.command_prefix}{command.name}", value=command.help, inline=False)
        await ctx.send(embed=embed)
