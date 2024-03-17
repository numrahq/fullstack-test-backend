import os
import urllib.parse

DB_USERNAME = urllib.parse.quote_plus(os.environ.get("DB_USERNAME", "postgres"))
DB_PASSWORD = urllib.parse.quote_plus(os.environ.get("DB_PASSWORD", "password"))
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")
DB_NAME = os.environ.get("DB_NAME", "autonifai")