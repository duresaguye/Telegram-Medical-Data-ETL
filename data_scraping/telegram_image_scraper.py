import logging
from telethon import TelegramClient
import csv
import os
import json
from dotenv import load_dotenv
# Set up logging
logging.basicConfig(
    filename='scraping.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Load environment variables once
load_dotenv('.env')

api_id = os.getenv('TG_API_ID')
api_hash = os.getenv('TG_API_HASH')
phone = os.getenv('phone')
# Create a folder for images
os.makedirs('telegram_images', exist_ok=True)

# Connect to Telegram
client = TelegramClient('anon', api_id, api_hash)

async def download_images():
    async with client:
        async for message in client.iter_messages("@lobelia4cosmetics"):
            if message.photo:
                file_path = await message.download_media('telegram_images/')
                print(f"Downloaded: {file_path}")

# Run the function
import asyncio
asyncio.run(download_images())
