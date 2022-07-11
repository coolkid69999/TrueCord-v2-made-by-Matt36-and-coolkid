import discord
from discord.ext import commands
import os
from . import *

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("help cog ready")
    
    @commands.command()
    async def cmd_list(self, ctx):
        cmdlist = "```"
        for command in self.client.commands:
            cmdlist += f"{command.name}\n{command.description}\n{command.usage}\n\n"
        await ctx.send(f"{cmdlist}```")
    