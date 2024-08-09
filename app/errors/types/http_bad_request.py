""" Module Http Bad Request Error """

from http import HTTPStatus


class HttpBadRequestError(Exception):
    """ Class Http Bad Request Error """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'BadRequest'
        self.status_code = HTTPStatus.BAD_REQUEST
