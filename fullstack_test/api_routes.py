from fastapi import FastAPI
from fullstack_test.api.invoice_api import InvoiceApi
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Fixing cors issues
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # since it's a test doesn't matter match specific domains
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "PATCH"],  # let do anything for
    allow_headers=["*"],  # Allow receive any header.
)

invoice_api = InvoiceApi()
app.include_router(invoice_api.router)
