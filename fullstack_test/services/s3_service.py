from fullstack_test.domain.invoice import Invoice
from fullstack_test.domain.orm import session_factory

# EXERCISE COMMENT:
# The idea of having an "interface" is that we don't need to think of the implementation details
#
# It DOES NOT imply multiple implementations but rather separating responsabilities in a way that will enables to swap implementations in the future, if we need it
#
# For the sake of time, this interface and concrete class will share same file
class ObjectStorageService:
    def read(self, path: str):
        pass

class S3Service(ObjectStorageService):
    # def __init__(self):
        # self.session = session_factory() if sf is None else sf

    def read(self, path: str):
        return path