import os
from dotenv import load_dotenv

load_dotenv()

CONFIG_API_KEY=os.getenv('API_KEY')
print(CONFIG_API_KEY)