import discord
from discord.ext import commands
import os


class Server(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Server cog ready")