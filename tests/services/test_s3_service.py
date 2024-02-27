from random import randint
from unittest import TestCase
from unittest.mock import Mock

from fullstack_test.services.s3_service import S3Service


class TestS3Service(TestCase):
    def test_that_it_returns_the_input(self):
        invoice_id = randint(1, 100)
        s3_service = S3Service()

        actual = s3_service.read(invoice_id)

        self.assertEqual(invoice_id, actual)
