""" Module Http Not Found Error """

from http import HTTPStatus


class HttpUnprocessableEntityError(Exception):
    """ Class Http Not Found Error """
    def __init__(self, message: str,  errors: list[dict[str, any]]):
        super().__init__(message)
        self.message = message
        self.name = 'Validation Error'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
        self.errors = errors

