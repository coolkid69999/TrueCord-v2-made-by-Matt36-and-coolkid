import requests 
import discord
from discord.ext import commands
import os
import colorama
from colorama import Fore, Style, init
import json
import datetime
import threading
from Cogs import Help, Server, Troll, Util, User

token = os.getenv('TOKEN')
prefix = "!"
client = commands.Bot(prefix, intents=discord.Intents.all(), self_bot=True, help_command=None)
headers = { "Authorization": f"{token}"}

def get_client():
    return client

@client.event
async def on_ready():
    print(f"ready on client {client.user.name}#{client.user.discriminator}")











cogHelp = Help.Help
cogServer = Server.Server
cogTroll = Troll.Troll
cogUtil = Util.Util
cogUser = User.User


client.add_cog(cogHelp(client))
client.add_cog(cogServer(client))
client.add_cog(cogTroll(client))
client.add_cog(cogUtil(client))
client.add_cog(cogUser(client))


client.run(token, bot=False)