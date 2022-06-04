#By the way this only has one command wich is Nuke
#also could you could add a error handler but im not going to because i want to keep it short
import discord
import os
import asyncio
import aiohttp
import json
from discord.ext import commands
from discord import File
import string
import io
import requests
import math
import threading

#Bot Prefix
client = commands.Bot(command_prefix='>',case_insensitive=True)
client.remove_command('help')

#Bot Online
@client.event
async def on_ready():
    print("Online")

#Clear Command
@client.command()
@commands.has_any_role('Owner')
async def Clear(ctx, amount=1000):
    clear = discord.Embed(title="Channel Nuked!", color=0xe61010)
    clear.add_field(name="NUKED!",value=" Channel Nuked")
    clear.set_image(url="https://images-ext-2.discordapp.net/external/QDzStf83v0EN-JX-dZEh_v4OPHzgVMITbZsmhaH7rL8/https/media.discordapp.net/attachments/838964678808961074/844624817180114974/standard_3.gif")
    await ctx.channel.purge(limit=amount)
    await ctx.send(embed=clear)
    
   
 #Bot Token
client.run('TOKEN')
