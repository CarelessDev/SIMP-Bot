from libraryimport import *


class SomeCrap(commands.Cog):
    """Category documentations"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        """Pong"""
        await ctx.send("Pong! tai")

    @commands.command(name='emoji', aliases=['e'])
    async def emoji(self, ctx):
        """emoji and shit"""
        emojis = ctx.bot.emojis

        await ctx.send(choice(emojis))
        '''for i in animated_emoji:
            await ctx.send(i)'''
