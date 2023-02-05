import os
from dotenv import load_dotenv

load_dotenv()

DJANGO_SECRET_KEY=str(os.getenv("DJANGO_SECRET_KEY"))
DEBUG=bool(os.getenv("DEBUG"))