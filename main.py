# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="BitbyBit v5.0 😻"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


@client.event
async def on_message(message):
    if message.content.startswith('!init 1'):
        embedVar = discord.Embed(
            title="Title", description="Desc", color=0x00fff0)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)


keep_alive()
client.run(os.getenv('TOKEN'))
