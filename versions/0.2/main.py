
import requests 
import discord
from discord.ext import commands
import os
import colorama
from colorama import Fore, Style, init
import json
import datetime
import threading
from Cogs import Help, Server, Troll, Util, User, Links, Localdata, Nuke, Scraping, Logging, Plugins
from Cogs.Plugins import *

token = os.getenv('TOKEN')
prefix = "!"
client = commands.Bot(prefix, intents=discord.Intents.all(), self_bot=True, help_command=None)
headers = { "Authorization": f"{token}"}

Help = Help.Help
Server = Server.Server
Troll = Troll.Troll
Util = Util.Util
Links = Links.Links
Localdata = Localdata.Localdata
Nuke = Nuke.Nuke
Scraping = Scraping.Scraping
Logging = Logging.Logging
User = User.User


def get_client():
    return client

@client.event
async def on_ready():
    print(f"ready on client {client.user.name}#{client.user.discriminator}")


@client.command()
async def unload(ctx, cog: str):
    try:
        client.remove_cog(cog)
    except:
        ctx.message.reply("Failed to find cog,")

@client.command()
async def load(ctx, cog):
    try:
        client.add_cog(cog(client))
    except:
        ctx.message.reply("Failed to find cog")



client.add_cog(Help(client))
client.add_cog(Server(client))
client.add_cog(Troll(client))
client.add_cog(Util(client))
client.add_cog(User(client))
client.add_cog(Links(client))
client.add_cog(Localdata(client))
client.add_cog(Nuke(client))
client.add_cog(Scraping(client))
client.add_cog(Logging(client))

client.run(token, bot=False)


#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins
#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins#plugins



