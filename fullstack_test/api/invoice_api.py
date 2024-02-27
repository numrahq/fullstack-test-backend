from fastapi import APIRouter

from fullstack_test.domain.orm import session_factory
from fullstack_test.repository.invoice_repository import InvoiceRepository


class InvoiceApi:
    def __init__(self, ir: InvoiceRepository = None):
        self.invoice_repository = InvoiceRepository(session_factory()) if ir is None else ir
        self.router = APIRouter()
        self.router.add_api_route("/invoices", self.get, methods=["GET"])
        self.router.add_api_route("/invoices/{invoice_id}/file", self.get_invoice_file, methods=["GET"])
        self.router.add_api_route("/invoices/{invoice_id}/approval", self.approve, methods=["POST"])
        self.router.add_api_route("/invoices/{invoice_id}/approval", self.reject, methods=["DELETE"])

    def get_invoice_file(self, invoice_id: int):
        return "hi"
    
    def get(self, invoice_id: int = None):
        if invoice_id is None:
            return self.invoice_repository.find_all()
        return self.invoice_repository.find_by_id(invoice_id)

    def approve(self, invoice_id: int):
        self.invoice_repository.update_status(invoice_id, 'APPROVED')

    def reject(self, invoice_id: int):
        self.invoice_repository.update_status(invoice_id, 'REJECTED')