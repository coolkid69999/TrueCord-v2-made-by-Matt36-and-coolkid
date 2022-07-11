import discord
from discord.ext import commands
import os
import requests
from . import *


class PluginManager(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Plugin cog ready")
    
    @commands.command()
    async def install(self, ctx, plugin_id):
        try:
            pr = requests.get(f"https://truecord-database.thechadcoders.repl.co/plugins/{plugin_id}")
            open("../main.py", "a").write(f"{plugin_id} = Cogs.PLugins.{plugin_id}\nclient.add_cog({plugin_id}(client))")
            open("./Plugins.py", "a").write(pr.text)
            await ctx.send("Plugin installed. It will activate next restart")
        except:
            await ctx.send("Plugin does not exist")

    @commands.command()
    async def plugin(self, ctx, plugin_id):
        embed = {

        }
        embed = discord.Embed.from_dict(embed)
        await ctx.send(embed=embed)

