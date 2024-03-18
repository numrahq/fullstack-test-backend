import boto3
from botocore import UNSIGNED
from botocore.config import Config

class InvoicePDFRepository:
  def __init__(self):
    self.bucket_name = "take-home-test-invoice-data"
    self.s3Client = boto3.client("s3", config=Config(signature_version=UNSIGNED))


  def get_by_number(self, invoice_number):
    response = self.s3Client.get_object(Bucket=self.bucket_name, Key=f"{invoice_number}.pdf")
    return response["Body"].read()

