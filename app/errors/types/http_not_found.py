""" Module Http Not Found Error """

from http import HTTPStatus


class HttpNotFoundError(Exception):
    """ Class Http Not Found Error """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'NotFound'
        self.status_code = HTTPStatus.NOT_FOUND
