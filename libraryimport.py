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
import asyncpraw
import numpy as np


SKITTLE_DICT = ["uwu", "blushes", "π£π­πΆπ΄π©π¦π΄", "(im a girl btw)", "γ΄γγ", "γ―γ³γ―γ³"]


def skittify(msg: str, skittiness: int = 0, firstchar: str = "") -> str:
    if skittiness <= 0:
        skittiness = random.randrange(3, 11)
    first_char = firstchar if len(firstchar) else msg[0].lower()
    return first_char + f"\n{first_char}-" * skittiness + f"\n*{first_char}~{first_char}{msg[1:]}*" + f"\n*{random.choice(SKITTLE_DICT)}*"
