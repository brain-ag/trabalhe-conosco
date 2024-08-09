""" Module Error Handler """

from http import HTTPStatus

from app.errors.types import (
    HttpBadRequestError,
    HttpNotFoundError,
    HttpBadApiRequestError,
    HttpUnprocessableEntityError,
    HTTPUniqueConstraintError,
    HttpFileUploadError,
    HttpUnsupportedMediaTypeError,
    HttpPayloadTooLargeError)
from app.presentation.http_types.http_response import HttpResponse
from app.errors.interfaces.logging_interface import LoggingInterface
import uuid


class ErrorHandler:
    """ Class Error Handler """

    def __init__(self, logging: LoggingInterface):
        self.error_uuid = []
        self.logging = logging

    def handle_errors(self, error: Exception) -> HttpResponse:
        """ Method to handle errors """
        print(error)
        self.__call_logging(error=error)

        if isinstance(error, (HttpBadRequestError,
                              HttpNotFoundError,
                              HTTPUniqueConstraintError,
                              HttpFileUploadError,
                              HttpUnsupportedMediaTypeError,
                              HttpPayloadTooLargeError)):  # incluir todas as proximas nesse if
            http_response = self.__http_response_personalized_error(error=error)

            return http_response

        elif isinstance(error, HttpBadApiRequestError):
            http_response = self.__http_response_bad_api_request_error(error=error)
            return http_response

        elif isinstance(error, HttpUnprocessableEntityError):
            http_response = self.__http_response_bad_unprocessable_entity_error(error=error)
            return http_response

        http_response = self.__http_response_unexpected_error(error=error)
        return http_response

    def __call_logging(self, error: Exception):
        # metodo joga pro logging
        # define o error_uuid
        self.logging.inform(error=error)
        self.error_uuid = [uuid.uuid4()]  # pego aqui com o logging

    def __http_response_personalized_error(self, error: Exception):
        """Recebe qualquer tipo personalizado de erro, ou seja, erro previsto"""
        http_response = HttpResponse(
            status_code=error.status_code,
            body={
                'type': error.name,
                'error_uuid': self.error_uuid,  # apenas por enquanto, posteriormente recebo do logging
                'message': error.message,
            },
        )
        return http_response

    def __http_response_bad_api_request_error(self, error: Exception):
        """Recebe o tipo HttpBadApiRequestError"""
        error.uuid += self.error_uuid
        http_response = HttpResponse(
            status_code=error.status_code,
            body={
                'type': error.name,
                'error_uuid': error.uuid,  # apenas por enquanto, posteriormente recebo do logging
                'message': error.message,
            },
        )
        return http_response

    def __http_response_bad_unprocessable_entity_error(self, error: Exception):
        """Recebe o tipo HttpUnprocessableEntityError"""
        http_response = HttpResponse(
            status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
            body={
                'type': 'UnprocessableEntity',
                'error_uuid': self.error_uuid,
                'title': error.message,
                'notifications': error.errors,  # Mantém a estrutura dos erros de validação
            },
        )
        return http_response

    def __http_response_unexpected_error(self, error: Exception):
        """Recebe algum Exception não esperado"""
        http_response = HttpResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            body={
                'type': 'Internal Server Error',
                'error_uuid': self.error_uuid,
                'message': 'Internal Server Error',
            },
        )
        return http_response
