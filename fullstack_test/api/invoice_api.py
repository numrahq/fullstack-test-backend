from fastapi import APIRouter

from fullstack_test.domain.orm import session_factory
from fullstack_test.repository.invoice_repository import InvoiceRepository


class InvoiceApi:
    def __init__(self, ir: InvoiceRepository = None):
        self.invoice_repository = InvoiceRepository(session_factory()) if ir is None else ir
        self.router = APIRouter()
        self.router.add_api_route("/invoices", self.get_all, methods=["GET"])

    def get_all(self):
        return self.invoice_repository.find_all()