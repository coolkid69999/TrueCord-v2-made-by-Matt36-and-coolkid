import discord
from discord.ext import commands
import os
from . import *

class Nuke(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("nuke cog ready")
    
    