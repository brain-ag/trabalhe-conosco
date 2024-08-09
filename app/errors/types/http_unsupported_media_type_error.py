""" Module Http Not Found Error """

from http import HTTPStatus


class HttpUnsupportedMediaTypeError(Exception):
    """ Class Http Payload too Large """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'UnsupportedMediaType'
        self.status_code = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
