import os

API_HOST = os.environ.get("API_HOST", "")
API_PORT = int(os.environ.get("API_PORT", ""))
API_ALLOWED_ORIGINS = os.environ.get("API_ALLOWED_ORIGINS", "").split(",")