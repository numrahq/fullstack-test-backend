from fastapi import FastAPI
from fullstack_test.api.invoice_api import InvoiceApi
from fastapi.middleware.cors import CORSMiddleware

from fullstack_test.api_config import API_ALLOWED_ORIGINS

app = FastAPI()

origins = API_ALLOWED_ORIGINS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

invoice_api = InvoiceApi()
app.include_router(invoice_api.router)
