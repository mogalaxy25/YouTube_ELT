import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")    

if not API_KEY:
    raise ValueError("YOUTUBE_API_KEY is not set in the environment variables.")

if not CHANNEL_ID:
    raise ValueError("YOUTUBE_CHANNEL_ID is not set in the environment variables.")