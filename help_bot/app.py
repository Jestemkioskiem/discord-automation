import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

client = Bot(description="Utopian-Bot", command_prefix='!', pm_help = False)

help_channel_id = "FOO" #click "copy id on the discord channel"
help_msg = "For technical support, issues with posts, suggestions for utopian.io and other inquiries, please contact the Utopian team at https://support.utopian.io/"

async def command(message,text):
        text = str(text)[1:]

#       if text.lower().startswith('help'):
#               await client.send_message(message.channel, help_msg)


async def send_help(channel_id):
        help_channel = client.get_channel(channel_id)
        last_message = await client.send_message(help_channel, help_msg)
        while True:
                counter = 0
                async for log in client.logs_from(help_channel, after=last_message):
                        counter+=1
                        if counter > 4: 
                                last_message = await client.send_message(help_channel, help_msg)
                                break
                await asyncio.sleep(5400)

@client.event
async def on_ready():
        await send_help(help_channel_id)

@client.event
async def on_message(message):
        if message.content.startswith(client.command_prefix): # Setting up commands. You can add new commands in the commands() function at the top of the code.
                await command(message, message.content)

client.run(os.getenv('UB_TOKEN')) # set an ENV variable UB_TOKEN to the discord token of the bot
