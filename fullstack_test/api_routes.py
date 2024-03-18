from fastapi import FastAPI
from fullstack_test.api.invoice_api import InvoiceApi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite solicitudes de estos orígenes
    allow_credentials=True,  # Permite cookies
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todas las cabeceras
)

invoice_api = InvoiceApi()
app.include_router(invoice_api.router)
