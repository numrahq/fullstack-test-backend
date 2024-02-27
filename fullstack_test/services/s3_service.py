from fullstack_test.services.aws_config import AWS_ACCESS_KEY, AWS_SECRET_KEY
import boto3

# EXERCISE COMMENT:
# The idea of having an "interface" is that we don't need to think of the implementation details
#
# It DOES NOT imply multiple implementations but rather separating responsabilities in a way that will enables to swap implementations in the future, if we need it
#
# For the sake of time, this interface and concrete class will share same file
class ObjectStorageService:
    def download(self, path: str):
        pass

class S3Service(ObjectStorageService):
    def __init__(self, bucket_name: str, aws_access_key = AWS_ACCESS_KEY, aws_secret_key = AWS_SECRET_KEY):
        if not (aws_access_key or aws_secret_key):
            raise ValueError("AWS credentials must be provided")
        if not bucket_name:
            raise ValueError("Bucket name must be provided")

        self.bucket_name = bucket_name
        self._s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    def download(self, path: str):
        file_content = self._download_from_s3(path)

        if file_content is None:
            raise ValueError("Failed to retrieve file from S3")

        return file_content

    def _download_from_s3(self, s3_key):
        try:
            response = self._s3.get_object(Bucket=self.bucket_name, Key=s3_key)
            return response['Body'].read()
        except:
            return None