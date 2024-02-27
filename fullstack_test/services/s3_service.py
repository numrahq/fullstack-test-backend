from fullstack_test.services.aws_config import AWS_ACCESS_KEY, AWS_SECRET_KEY

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
    # def __init__(self):
        # self.session = session_factory() if sf is None else sf

    def download(self, path: str):
        return f"{path}_{AWS_ACCESS_KEY}_{AWS_SECRET_KEY}"