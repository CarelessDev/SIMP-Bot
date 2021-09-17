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
    async def emoji(self, ctx, *, names: str = None):
        """emoji and shit"""
        emojis = ctx.bot.emojis
        A_em = []
        N_em = []
        for i in emojis:
            if i.animated:
                A_em.append(i)
            else:
                N_em.append(i)

        name_list = names.split() if names else []   
        await ctx.send(choice(A_em))
        '''for i in animated_emoji:
            await ctx.send(i)'''