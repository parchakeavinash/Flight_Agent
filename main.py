import os

from dotenv import load_dotenv
from pathlib import Path


Script_path = Path(__file__).resolve().parent
env_path = Script_path / '.env'

load_dotenv(env_path)
