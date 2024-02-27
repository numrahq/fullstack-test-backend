import os
from random import randint
from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock

from fullstack_test.services.s3_service import S3Service

class TestS3Service(TestCase):
    @patch("boto3.client")
    def test_download_success(self, mock_boto3_client):
        # Mock the S3 client
        mock_s3 = MagicMock()
        mock_boto3_client.return_value = mock_s3

        # Configure the mock_s3 to return a simulated PDF content
        simulated_pdf_content = b"Simulated PDF Content"
        mock_s3.get_object.return_value = {'Body': MagicMock(read=MagicMock(return_value=simulated_pdf_content))}

        bucket_name = "test"
        aws_access_key="access"
        aws_secret_key="secret"

        # Create an instance of S3Service
        s3_service = S3Service(bucket_name, aws_access_key, aws_secret_key)

        # Call the download_pdf method
        invoice_id = randint(1, 100)
        pdf_content = s3_service.download(invoice_id)

        # Assertions
        mock_boto3_client.assert_called_with('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        mock_s3.get_object.assert_called_with(Bucket=bucket_name, Key=invoice_id)
        self.assertEqual(pdf_content, simulated_pdf_content)

    @patch("boto3.client")
    def test_download_failure(self, mock_boto3_client):
        # Mock the S3 client
        mock_s3 = MagicMock()
        mock_boto3_client.return_value = mock_s3

        # Configure the mock_s3 to thrown
        mock_s3.get_object.side_effect = Exception("Simulated S3 Error")
        # simulated_pdf_content = b"Simulated PDF Content"
        # mock_s3.get_object.return_value = {'Body': MagicMock(read=MagicMock(return_value=simulated_pdf_content))}

        bucket_name = "test"
        aws_access_key="access"
        aws_secret_key="secret"

        # Create an instance of S3Service
        s3_service = S3Service(bucket_name, aws_access_key, aws_secret_key)

        invoice_id = randint(1, 100)

        with self.assertRaises(ValueError) as context:
            s3_service.download(invoice_id)

        # Call the download_pdf method

        # Assertions
        mock_boto3_client.assert_called_with('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        mock_s3.get_object.assert_called_with(Bucket=bucket_name, Key=invoice_id)
        self.assertEqual(str(context.exception), "Failed to retrieve file from S3")