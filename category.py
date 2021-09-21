from discord import utils
from libraryimport import *
from redd import *
from urllib.request import urlopen
import io
from PIL import Image


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
      
    @commands.command(name='gay')
    async def gay(self, ctx, *, who:str = None):
        """gay"""
        if who:
            await ctx.send(skittify(f'{who} is gay!'))
        else:
            await ctx.send(skittify('You are gay'))
      
    @commands.command(name='reddit', aliases=['r',  'r/'])
    async def reddit(self, ctx, *, req:str = None):
        """use simpreddit <subreddit> <search>"""
        msg = await ctx.send('Loading ... ')
        emj = utils.get(ctx.bot.emojis, name="fuckyou")
        if req:
            search = req.split()
            subreddit = await reddit.subreddit(search[0])   
            if len(search) > 1:
                r = []
                async for i in subreddit.search(str(search[1:]), limit=5):
                    r.append(i)
                random_sub = choice(r)                
            else:
                random_sub = await subreddit.random()
        else:
            subreddit = await reddit.subreddit('arknights') 
            random_sub = await subreddit.random()

    

        name = random_sub.title
        url = random_sub.url
        ups = random_sub.score
        link = random_sub.permalink
        comments = random_sub.num_comments

        emb = discord.Embed(title="here some sauce", description=f'```css\n{name}\n```', color=0xf1c40f)
        emb.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
        
        
        
        if random_sub.over_18:
            img = Image.open(urlopen(url))
            img.save('SPOILER_img.jpg')
            file = discord.File('SPOILER_img.jpg', spoiler=True)
            emb.set_footer(text='18+ huh You disgusting fuck')
            

            await msg.edit(content=f'{emj} <https://reddit.com{link}> {emj}', embed = emb) 
            await ctx.send(file = file )
            await msg.add_reaction(emj)
            os.remove('SPOILER_img.jpg')
        else:
            await msg.edit(content=f'<https://reddit.com{link}> :white_check_mark:') 
            emb.set_footer(text='Here is your meme!')
            emb.set_image(url=url)
            await ctx.send(embed = emb)

        
        subreddit = reddit.subreddit()
        




    