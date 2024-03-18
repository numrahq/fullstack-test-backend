from fastapi import APIRouter, Response

from fullstack_test.domain.orm import session_factory
from fullstack_test.repository.invoice_repository import InvoiceRepository
from fullstack_test.repository.invoice_pdf_repository import InvoicePDFRepository


class InvoiceApi:
    def __init__(self, ir: InvoiceRepository = None):
        self.invoice_repository = InvoiceRepository(session_factory()) if ir is None else ir
        self.invoice_pdf_repository = InvoicePDFRepository()
        self.router = APIRouter()
        self.router.add_api_route("/invoices", self.get, methods=["GET"])
        self.router.add_api_route("/invoices/{invoice_id}/approval", self.approve, methods=["POST"])
        self.router.add_api_route("/invoices/{invoice_id}/approval", self.reject, methods=["DELETE"])
        self.router.add_api_route("/invoices/{invoice_number}/pdf", self.get_pdf, methods=["GET"])

    def get(self, invoice_id: int = None):
        if invoice_id is None:
            return self.invoice_repository.find_all()
        return self.invoice_repository.find_by_id(invoice_id)

    def approve(self, invoice_id: int):
        self.invoice_repository.update_status(invoice_id, 'APPROVED')

    def reject(self, invoice_id: int):
        self.invoice_repository.update_status(invoice_id, 'REJECTED')

    def get_pdf(self, invoice_number: str):
        pdf_content = self.invoice_pdf_repository.get_by_number(invoice_number)
        
        return Response(content=pdf_content, media_type="application/pdf")