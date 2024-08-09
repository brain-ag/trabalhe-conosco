""" Module Http Not Found Error """

from http import HTTPStatus


class HttpPayloadTooLargeError(Exception):
    """ Class Http Payload too Large """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'PayloadTooLarge'
        self.status_code = HTTPStatus.REQUEST_ENTITY_TOO_LARGE
