import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "+")

@client.event
async def on_ready():
    print("Bot is ready!")
    await client.change_presence(game=discord.Game(name="In Beta Dont Use To Many Commands!"))

@client.event
async def on_message (message):
    if message.content.startswith('+hello'):
        msg = 'Hello {0.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+bye'):
        msg = 'Goodbye {0.author.mention} Hope To See You Soon :wave:'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+help'):
        msg = 'Contacting The Owner <@344967220025098242> Someone Needs Help!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+commands'):
        msg = ' {0.author.mention} The Bot Commands are `+hello` `+bye` `+help` `+invite` `+feedback` `+commands` More Comeing Soon!'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+invite'):
        msg = 'Want To Invte Me To Your Discord Press This Link https://goo.gl/7AeAH1'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('+feedback'):
        msg = 'To Give Feedback Join The Creators Discord https://discord.gg/hbgVy88'.format(message)
        await client.send_message(message.channel, msg)
        


client.run ("Put Bot Token Here")
