import enum
import os


class ExceptionType(enum.Enum):
    NOT_REQUIRED_FILE_TYPE = '.CSV'
    NO_SUCH_FILE = 'no file'
    HEADER_ERROR = 'Header error'


class CensusAnalyserException(Exception):  # user defined exceptions

    def __init__(self, exception_type, message):
        self.message = message
        self.ExceptionType = exception_type


def check_exceptions_type(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    try:
        if file_extension == ".json":
            raise CensusAnalyserException(ExceptionType.NOT_REQUIRED_FILE_TYPE, "wrong file type")
    except FileNotFoundError:
        raise CensusAnalyserException(ExceptionType.NO_SUCH_FILE, "No such file")
    except RuntimeError:
        raise CensusAnalyserException(ExceptionType.HEADER_ERROR, "Error in Header")


