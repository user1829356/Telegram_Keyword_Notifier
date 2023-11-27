"""
Telegram Keyword Searcher

This script searches for specific keywords in specified Telegram channels and prints out messages containing those keywords.

Steps to use this script:

1. REQUIREMENTS:
   - Python 3.x (https://www.python.org/downloads/)
   - `telethon` library. Install via pip:
     $ pip install telethon
   - `pytz` library. Install via pip:
     $ pip install pytz

2. SETTING UP TELEGRAM API:
   a. Go to https://my.telegram.org and log in with your Telegram phone number.
   b. Click on 'API development tools' and fill out the form.
   c. You will receive your `api_id` and `api_hash`. Copy them.

3. MODIFY THE SCRIPT:
   a. Replace 'YOUR_API_ID' and 'YOUR_API_HASH' in the script with the values obtained from step 2.
   b. Replace 'YOUR_PHONE_NUMBER' with your phone number in international format.
   c. Modify the `key_words` list to contain the keywords you want to search for.
   d. Add the channel IDs to 'channels.txt', one ID per line. Channels require -100 added to the beginning of the ID, for example if a channel ID was 123456789, it should be -100123456789 in the text file.

4. RUNNING THE SCRIPT:
   a. Save the script.
   b. Run the script using:
     $ python3 your_script_name.py
   c. If you're running the script for the first time, you'll need to enter phone number in international format and the verification code received on Telegram.

5. RESULTS:
   The script will print out any message from the last two hours in the specified channels that contain any of the keywords. If longer or shorter time needed, please modify.

NOTE: The search is case-insensitive. For example, searching for 'test1' will also find 'Test1' or 'TEST1'.

"""

import asyncio
import pytz
import logging
from datetime import datetime, timedelta
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import ChannelPrivateError

# Set up logging configuration
logging.basicConfig(filename="telegram_searcher.log", level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Telegram app credentials
api_id = 'YOUR_API_ID'  # replace with your API ID from step 2
api_hash = 'YOUR_API_HASH'  # replace with your API HASH from step 2
phone_number = 'YOUR_PHONE_NUMBER'  # replace with your phone number in international format
key_words = ['test1', 'test2']

def load_channel_ids_from_file(filename):
    with open(filename, 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

async def check_messages(client, words, channels):
    utc_now = datetime.now(pytz.utc)
    two_hours_ago = utc_now - timedelta(hours=2) #modify if needed

    with open('telegram_keyword_searcher_results.txt', 'a') as results_file:
        for word in words:
            for channel_id in channels:
                try:
                    channel_details = await client.get_entity(channel_id)
                    channel_title = channel_details.title if channel_details and hasattr(channel_details, 'title') else str(channel_id)

                    async for message in client.iter_messages(channel_id, limit=100):
                        if message.date > two_hours_ago and message.text and word.lower() in message.text.lower():
                            results_file.write(f"Found '{word}' in channel {channel_title} at {message.date}: {message.text}\n")
                except ChannelPrivateError:
                    logger.warning(f"Can't access channel {channel_id} because it's private or you're not a member.")
                except Exception as e:
                    logger.error(f"Error processing channel {channel_id}: {e}")

async def main():
    channels = load_channel_ids_from_file('telegram_channels.txt')

    async with TelegramClient('anon', api_id, api_hash) as client:
        if not await client.is_user_authorized():
            await client.send_code_request(phone_number)
            verification_code = input("Enter the code you received: ")
            await client.sign_in(phone_number, verification_code)

        await check_messages(client, key_words, channels)

if __name__ == '__main__':
    asyncio.run(main())
