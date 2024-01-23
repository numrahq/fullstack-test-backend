from fullstack_test.domain.invoice import Invoice
from fullstack_test.domain.orm import session_factory


class InvoiceRepository:
    def __init__(self, sf):
        self.session = session_factory() if sf is None else sf

    def find_all(self):
        with self.session:
            return self.session.query(Invoice).all()

    def find_by_id(self, invoice_id):
        with self.session:
            return self.session.query(Invoice) \
                .filter_by(id=invoice_id) \
                .first()

    def update_status(self, invoice_id, new_status):
        with self.session:
            self.session.query(Invoice) \
                .filter_by(id=invoice_id) \
                .update({"status": new_status})
            self.session.commit()


