from random import randint
from unittest import TestCase
from unittest.mock import Mock

from fullstack_test.api.invoice_api import InvoiceApi

# EXERCISE NOTE

# I've used fake_invoice in this test to hide the domain from the API testing
class TestInvoiceApi(TestCase):
    def test_that_get_returns_same_as_mock_with_parameter(self):
        invoice_repository = Mock()
        s3_service = Mock()
        invoice_api = InvoiceApi(invoice_repository, s3_service)

        expected = [{"number": "INV-123", "description": "x2 MacBook Pro", "payment_terms": 30}]
        invoice_repository.find_by_id.return_value = expected

        actual = invoice_api.get(randint(0, 100))

        self.assertEqual(expected, actual)

    def test_that_get_returns_same_as_mock_without_parameter(self):
        invoice_repository = Mock()
        s3_service = Mock()
        invoice_api = InvoiceApi(invoice_repository, s3_service)

        expected = [{"number": "INV-123", "description": "x2 MacBook Pro", "payment_terms": 30}]
        invoice_repository.find_all.return_value = expected

        actual = invoice_api.get(None)

        self.assertEqual(expected, actual)

    def test_that_approve_invokes_repository(self):
        invoice_id = randint(1, 100)
        invoice_repository = Mock()
        s3_service = Mock()
        invoice_api = InvoiceApi(invoice_repository, s3_service)

        expected = [{"number": "INV-123", "description": "x2 MacBook Pro", "payment_terms": 30}]
        invoice_repository.find_all.return_value = expected

        invoice_api.approve(invoice_id)

        invoice_repository.update_status.assert_called_once_with(invoice_id, 'APPROVED')

    def test_that_reject_invokes_repository(self):
        invoice_id = randint(1, 100)
        invoice_repository = Mock()
        s3_service = Mock()
        invoice_api = InvoiceApi(invoice_repository, s3_service)

        expected = [{"number": "INV-123", "description": "x2 MacBook Pro", "payment_terms": 30}]
        invoice_repository.find_all.return_value = expected

        invoice_api.reject(invoice_id)

        invoice_repository.update_status.assert_called_once_with(invoice_id, 'REJECTED')

    def test_that_get_invoice_file_returns_data(self):
        expected = randint(1, 100)
        invoice_repository = Mock()
        s3_service = Mock()
        invoice_api = InvoiceApi(invoice_repository, s3_service)

        number = "INV-123"
        invoice = type("fake_invoice", (object,), { "number": number })

        invoice_repository.find_by_id.return_value = invoice
        s3_service.download.return_value = expected

        actual = invoice_api.get_invoice_file(randint(0, 100))

        s3_service.download.assert_called_once_with(number)
        self.assertEqual(expected, actual)

    def test_that_get_invoice_file_fails(self):
        invoice_repository = Mock()
        s3_service = Mock()
        invoice_api = InvoiceApi(invoice_repository, s3_service)

        invoice = None

        invoice_repository.find_by_id.return_value = invoice

        with self.assertRaises(AttributeError):
            invoice_api.get_invoice_file(randint(0, 100))

        s3_service.download.assert_not_called()