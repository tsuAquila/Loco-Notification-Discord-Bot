import discord
from discord.ext import commands, tasks
import os
from keep_alive import keep_alive
import asyncio
from locoAPI import stream

client = commands.Bot(command_prefix='%', intents=discord.Intents.all())

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
    

client.run('OTI4Mjk5NzgwMzkwNjYyMjI2.YdWwig.TIR9hFL7XvGmYl1JxeogZvpZ0Hk')