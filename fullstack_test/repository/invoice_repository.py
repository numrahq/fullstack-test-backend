from fullstack_test.domain.invoice import Invoice
from fullstack_test.domain.orm import session_factory


class InvoiceRepository:
    def __init__(self, sf):
        self.session = session_factory() if sf is None else sf

    def find_all(self):
        with self.session:
            return self.session.query(Invoice).all()