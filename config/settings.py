import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
API_BASE_URL = os.getenv("API_BASE_URL", "https://reqres.in/api")
DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "10000"))
HEADLESS = os.getenv("HEADLESS", "true").lower() not in {"0", "false", "no"}
