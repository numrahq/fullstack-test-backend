import os
import urllib.parse

AWS_ACCESS_KEY = urllib.parse.quote_plus(os.environ.get("AWS_ACCESS_KEY", ""))
AWS_SECRET_KEY = urllib.parse.quote_plus(os.environ.get("AWS_SECRET_KEY", ""))
AWS_INVOICES_BUCKET = urllib.parse.quote_plus(os.environ.get("AWS_INVOICES_BUCKET", ""))