from random import choice
import asyncio
import functools
import itertools
import math
import random
import os
import discord
import youtube_dl
from discord.utils import get
from async_timeout import timeout
from discord.ext import commands, tasks
from dotenv import load_dotenv


SKITTLE_DICT = ["uwu", "blushes", "𝘣𝘭𝘶𝘴𝘩𝘦𝘴", "(im a girl btw)"]


def skittify(msg: str, skittiness: int = random.randrange(3, 11)) -> str:
    first_char = msg[0].lower()
    return first_char + f"\n{first_char}-" * skittiness + f"\n*{first_char}~{first_char}{msg[1:]}*" + f"\n*{random.choice(SKITTLE_DICT)}*"
