from fastapi import FastAPI
from fullstack_test.api.invoice_api import InvoiceApi

app = FastAPI()

invoice_api = InvoiceApi()
app.include_router(invoice_api.router)
