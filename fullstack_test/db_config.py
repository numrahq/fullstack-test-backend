import os
import urllib.parse

DB_USERNAME = urllib.parse.quote_plus(os.environ.get("DB_USERNAME", ""))
DB_PASSWORD = urllib.parse.quote_plus(os.environ.get("DB_PASSWORD", ""))
DB_HOST = os.environ.get("DB_HOST", "")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "")