import discord
from discord.ext import commands, tasks
import os
import asyncio
from locoAPI import stream
from config.json import TOKEN

client = commands.Bot(command_prefix='%', intents=discord.Intents.all())

stream("sc0utOP")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Activity(
                                     type=discord.ActivityType.watching,
                                     name='Over this Server'))
    print('Logged in as {0.user}'.format(client))

@client.command()
async def setup(ctx, channel, streamerID):
    loco(streamerID)
    

client.run(os.environ("TOKEN"))