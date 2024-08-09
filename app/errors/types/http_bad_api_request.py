""" Module Http Bad Request Error """

from http import HTTPStatus
import uuid


class HttpBadApiRequestError(Exception):
    """ Class Http Bad Request Error """

    def __init__(self, message: str, uuid_error: list[uuid.UUID]):
        super().__init__(message)
        self.message = message
        self.name = 'BadRequest'
        self.status_code = HTTPStatus.BAD_REQUEST
        self.uuid = uuid_error

