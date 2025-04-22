# AnshiBot/config.py

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 12345))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
OWNER_ID = int(os.getenv("OWNER_ID", 123456789))
START_IMG_URL = os.getenv("START_IMG_URL", "https://example.com/image.jpg")
