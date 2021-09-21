from libraryimport import *
from music import Music
from category import SomeCrap


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


def setup(bot):
    bot.add_cog(SomeCrap(bot))
    bot.add_cog(Music(bot))


bot = commands.Bot(command_prefix='simp')
setup(bot)


@bot.event
async def on_ready():
    print('S~Skittle i..is ready!')
    change_status.start()


@tasks.loop(seconds=300)
async def change_status():
    status: str = 'Caffe Latte Caffe Mocha Cappuchino'
    activity: discord.Activity = discord.Activity(
        type=discord.ActivityType.listening, name=status)
    await bot.change_presence(activity=activity)


bot.run(TOKEN)
