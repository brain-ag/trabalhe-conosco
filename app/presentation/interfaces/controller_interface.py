""" Module Controller Interface """

from abc import ABC, abstractmethod

from app.presentation.http_types import HttpRequest, HttpResponse


class ControllerInterface(ABC):
    """ Class Controller Interface """
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        """ Class Handle HTTP request """
        pass
