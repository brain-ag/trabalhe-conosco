# mypy: disable-error-code=import-untyped

""" Module Django Request Adapter """

import json

from django.core.handlers.wsgi import WSGIRequest

from app.presentation.http_types import HttpRequest, HttpResponse
from app.presentation.interfaces.controller_interface import ControllerInterface


class DjangoRequestAdapter:

    """ Class Django Request Adapter. Classe que recebe um request django WSGI, converte para o tipo HttpRequest.
     Recebe também o objeto do controller (que implementa a interface controller) que será utilizada.
     Esse controller recebe como parametro o HttpRequest gerado e na sequência devolve o httpresponse"""

    def adapt(self, request: WSGIRequest, controller: ControllerInterface) -> HttpResponse:
        """ Method adapt """

        files = {}

        body = json.loads(request.body) if request.body else {}

        headers = request.headers
        query_params = request.GET
        url = request.path
        ipv4 = request.META.get('REMOTE_ADDR')
        path_params = request.resolver_match.kwargs

        http_request = HttpRequest(
            headers=headers, body=body, query_params=query_params, url=url, ipv4=ipv4, path_params=path_params,
            files=files
        )

        http_response = controller.handle(http_request)
        return http_response
