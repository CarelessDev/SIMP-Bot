from discord import utils
from libraryimport import *


class Skittle_talk(commands.Cog):
    """talking with skittle chan yay"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send(skittify('An error occurred: {}'.format(str(error))))
    

    @commands.command(name='talk', alias=['t'])
    async def talk(self, ctx, *, message:str = None):
        """skittle-chan introduction"""
        
    

   