import discord
import time
import calendar
import pymysql
from PIL import Image, ImageDraw, ImageSequence, ImageFont
import os
import re
import random
from random import randint
import math
import schedule
import asyncio
from multiprocessing import Process
import numpy as np
import requests
import string
from collections import defaultdict
from discord.ext.commands import Bot
from better_profanity import profanity

# Compatibility stubs replacing the removed discord-components library.
# These hold component properties; AwaitView in disccomm.py converts them to
# discord.py 2.0 ui.View items at send time.
class DiscordComponents:
    def __init__(self, bot): pass

_BUTTON_STYLES = {
    1: discord.ButtonStyle.primary,
    2: discord.ButtonStyle.secondary,
    3: discord.ButtonStyle.success,
    4: discord.ButtonStyle.danger,
}

class Button:
    def __init__(self, label='', style=1, id=None, disabled=False, emoji=None):
        self.label = label
        self.style = style   # kept as int; AwaitView converts on build
        self.custom_id = id
        self.disabled = disabled
        self.emoji = emoji

class Select:
    def __init__(self, options=None, placeholder='', disabled=False):
        self.options = options or []
        self.placeholder = placeholder
        self.disabled = disabled

def SelectOption(label, value, description=None):
    return discord.SelectOption(
        label=str(label)[:100],
        value=str(value)[:100],
        description=str(description)[:100] if description is not None else None,
    )

ActionRow = list

def mixedCase(*args):
  total = []
  import itertools
  for string in args:
    a = map(''.join, itertools.product(*((c.upper(), c.lower()) for c in       string)))
    for x in list(a): total.append(x)
  return list(total)
activeUsers = []
activity = discord.Activity(type=discord.ActivityType.listening, name="ab help")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = Bot(case_insensitive=True, activity=activity, help_command=None, command_prefix=mixedCase("ab "), intents=intents)
