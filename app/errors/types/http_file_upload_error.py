""" Module Http Not Found Error """

from http import HTTPStatus


class HttpFileUploadError(Exception):
    """ Class Http File Upload Error """
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = 'FileUploadError'
        self.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
