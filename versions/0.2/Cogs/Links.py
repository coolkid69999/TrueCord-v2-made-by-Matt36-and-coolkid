import discord
from discord.ext import commands
import os
from . import *

class Links(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("links cog ready")
    
    