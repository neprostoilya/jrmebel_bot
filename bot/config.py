import os
from dotenv import load_dotenv

load_dotenv()

# BOT TOKEN 
TOKEN = os.getenv('BOT_TOKEN')
# ADMIN CHAT ID
ADMIN = os.getenv('BOT_ADMIN')
# URL API
URL = os.getenv('API_HOST')
# BOT PK
BOT_PK = os.getenv('BOT_PK')
# MANAGER GROUP
MANAGER = os.getenv('MANAGER')