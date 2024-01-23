from unittest import TestCase
from unittest.mock import Mock

from random import randint

from fullstack_test.api.invoice_api import InvoiceApi


class TestInvoiceApi(TestCase):

    def test_that_get_all_returns_same_as_mock(self):
        invoice_repository = Mock()
        invoice_api = InvoiceApi(invoice_repository)

        expected = [{"number": "INV-123", "description": "x2 MacBook Pro", "payment_terms": 30}]
        invoice_repository.find_all.return_value = expected

        actual = invoice_api.get_all()

        self.assertEqual(expected, actual)

    def test_that_get_returns_same_as_mock(self):
        invoice_repository = Mock()
        invoice_api = InvoiceApi(invoice_repository)

        expected = [{"number": "INV-123", "description": "x2 MacBook Pro", "payment_terms": 30}]
        invoice_repository.find_by_id.return_value = expected

        actual = invoice_api.get(randint(0, 100))

        self.assertEqual(expected, actual)