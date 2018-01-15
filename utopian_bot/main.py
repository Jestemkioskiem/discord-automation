import logging
import os
import re

from discord.ext.commands import Bot
from utopian_api.client import Client as UtopianClient

logger = logging.getLogger('Utopian Bot')
logger.setLevel(logging.INFO)
logging.basicConfig()


client = Bot(description="utopian-bot",
             command_prefix="$", pm_help=False)

utopian_client = UtopianClient()


@client.event
async def on_ready():
    logger.info("Logged in")


@client.event
async def on_message(message):
    if message.channel.name == "i-am-on-it":
        async for m in client.logs_from(message.channel, limit=100):
            if not m.content.startswith("https://utopian.io"):
                await client.delete_message(m)
            posts = re.findall(
                'https://utopian.io/utopian-io/@([^/]*)/(.[^\s]*)', m.content)
            posts = list(set(posts))
            for author, permlink in posts:
                utopian_post = UtopianClient().post(author, permlink)

                moderation_info = utopian_post.get(
                    "json_metadata", {}).get("moderator", {})
                if moderation_info:
                    reviewed = moderation_info.get("reviewed")
                    flagged = moderation_info.get("flagged")
                    if reviewed or flagged:
                        try:
                            await client.delete_message(m)
                        except Exception as error:
                            logger.error(error)
                            continue


def run():
    client.run(os.getenv("BOT_TOKEN"))

if __name__ == '__main__':
    run()
