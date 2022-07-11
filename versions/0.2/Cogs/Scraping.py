import discord
from discord.ext import commands
import os
from . import *
from threading import Thread
import datetime
from urlextract import URLExtract
tz = None
from flask import Flask, render_template
extractor = URLExtract()
class Scraping(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.theme = "Dark"
        self.logging = []
    @commands.Cog.listener()
    async def on_ready(self):
        print("scraping cog ready")
    
    @commands.command()
    async def exportersettings(self, ctx):
        await ctx.message.edit("")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in self.logging:
            self.writemessage(message, str(message.channel.id))

    def writemessage(self, message, name):
          r = open("base.txt", "r").read()
          f = open(f"./html/{name}.html", "a")
          f.write(r)
          html = self.create_message(message)
          for mention in message.mentions:
            try:
              html = html.replace(f'<@{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
              html = html.replace(f'<@!{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
            except:
              pass
          for mention in message.role_mentions:
            try:
              html = html.replace(f'<@{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
              html = html.replace(f'<@!{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
            except:
              pass
          urls = extractor.find_urls(message.content)
          for url in urls:
            html = html.replace(url, f'<a href="{url}">{url}</a>')
          html = html.replace(f'@here', f'<span class="mention" title="@here">@here</span>')
          html = html.replace(f'@everyone', f'<span class="mention" title="@everyone">@everyone</span>')
          f.write(html)

    def create_message(self, message):
        return f'''
                 <div class="chatlog__message-group">
                   <div class="chatlog__author-avatar-container">
                       <img class="chatlog__author-avatar" src="{message.author.avatar_url}" alt="Avatar">
                   </div>
                   <div class="chatlog__messages">
                       <span class="chatlog__author-name" title="{message.author.name}#{message.author.discriminator}" data-user-id="{message.author.id}" style="color: rgb({message.author.colour.r},{message.author.colour.g},            {message.author.colour.b})">{message.author.name}</span>


                       <span class="chatlog__timestamp">{message.created_at.day}-{message.created_at.month}-{message.created_at.year} {message.created_at.hour}:{message.created_at.minute}</span>

                           <div class="chatlog__message " data-message-id="{message.id}" id="message-{message.id}">
                                   <div class="chatlog__content">
                                       <div class="markdown">
                                           <span class="preserve-whitespace">{message.content}</span>

                                       </div>
                                   </div>
                           </div>
                   </div>
                 </div>
            '''

    @commands.command()
    async def addlogger(self, ctx, channel=None):
        if channel is None:
            channel = ctx.channel.id
        await ctx.message.delete()
        await ctx.send(f"Added logger to channel: {ctx.channel.name} {ctx.channel.id}")

    @commands.command()
    async def loglast(self, ctx, amount: int = 50, name: str = datetime.datetime.now(tz)):
        messages = await ctx.channel.history(limit=amount).flatten()
        messages.reverse()
        r = open("base.txt", "r").read()
        f = open(f"htmllogs/{name}.html", "a")
        f.write(r)
        for message in messages:
          html = self.create_message(message)
          for mention in message.mentions:
            try:
              html = html.replace(f'<@{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
              html = html.replace(f'<@!{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
            except:
              pass
          for mention in message.role_mentions:
            try:
              html = html.replace(f'<@{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
              html = html.replace(f'<@!{mention.id}>', f'<span class="mention" title="{mention.name}#{mention.discriminator}">@{mention.name}</span>')
            except:
              pass
          urls = extractor.find_urls(message.content)
          for url in urls:
            html = html.replace(url, f'<a href="{url}">{url}</a>')
          html = html.replace(f'@here', f'<span class="mention" title="@here">@here</span>')
          html = html.replace(f'@everyone', f'<span class="mention" title="@everyone">@everyone</span>')
          f.write(html)
        f.write(f"""
        </div>
        <div class="postamble">
            <div class="postamble__entry">Exported {amount} message(s)</div>
        </div>
        </body>
        </html>"""
        )
        app = Flask(__name__)
        @app.route("/")
        def home():
            return open(f"htmllogs/{name}.html", "r").read()
        app.run(host="0.0.0.0", port=8080)