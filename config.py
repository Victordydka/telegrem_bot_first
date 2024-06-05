import os           #чтобы работать(открывать) файлы
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('API_KEY')

