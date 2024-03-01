import os
from random import randint
from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock

from fullstack_test.services.s3_service import S3Service

class TestS3Service(TestCase):
    @patch("boto3.client")
    @patch("fastapi.responses.StreamingResponse")
    def test_download_success(self, mock_streaming_response, mock_boto3_client):
        pdf = iter([b'mock_chunk1', b'mock_chunk2'])
        # Mocking boto3.client
        mock_s3_client = mock_boto3_client.return_value
        mock_s3_client.get_object.return_value = {
            'Body': MagicMock(iter_chunks=MagicMock(return_value=pdf)),
            'ContentType': 'application/pdf'
        }

        # Configure StreamingResponse mock
        mock_streaming_response_instance = mock_streaming_response.return_value
        mock_streaming_response_instance.__iter__.return_value = pdf
        mock_streaming_response_instance.media_type = 'application/pdf'
        
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
        mock_s3_client.get_object.assert_called_with(Bucket="", Key=f"{bucket_name}/{invoice_id}")

    @patch("boto3.client")
    @patch("fastapi.responses.StreamingResponse")
    def test_download_failure(self, mock_streaming_response, mock_boto3_client):
        pdf = iter([b'mock_chunk1', b'mock_chunk2'])
        # Mocking boto3.client
        mock_s3_client = mock_boto3_client.return_value
        mock_s3_client.get_object.side_effect = Exception("Simulated S3 Error")

        # Configure StreamingResponse mock
        mock_streaming_response_instance = mock_streaming_response.return_value
        mock_streaming_response_instance.__iter__.return_value = pdf
        mock_streaming_response_instance.media_type = 'application/pdf'

        bucket_name = "test"
        aws_access_key="access"
        aws_secret_key="secret"

        # Create an instance of S3Service
        s3_service = S3Service(bucket_name, aws_access_key, aws_secret_key)

        # Call the download_pdf method
        invoice_id = randint(1, 100)

        with self.assertRaises(ValueError) as context:
            s3_service.download(invoice_id)

        # Assertions
        mock_boto3_client.assert_called_with('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
        mock_s3_client.get_object.assert_called_with(Bucket="", Key=f"{bucket_name}/{invoice_id}")
        self.assertEqual(str(context.exception), "Failed to retrieve file from S3")