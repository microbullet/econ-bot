""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

import random

from helpers import checks, db_manager

jobs = [""]

class Economy(commands.Cog, name="economy"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="work",
        description="Work for money",
    )
    @checks.not_blacklisted()
    @checks.registered()
    async def work(
        self, context: Context, user: Context.author
    ) -> None:
        money = random.randint(43, 223)
        context.send(f'{money}')
        db_manager.add_money(user, money)
        context.send()
        

async def setup(bot):
    await bot.add_cog(Economy(bot))
