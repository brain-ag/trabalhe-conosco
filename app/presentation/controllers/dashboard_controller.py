from app.domain.use_cases.dashboard import Dashboard
from app.presentation.http_types import HttpRequest, HttpResponse
from app.presentation.interfaces.controller_interface import ControllerInterface


from http import HTTPStatus


class DashboardController(ControllerInterface):

    def __init__(self, use_case: Dashboard):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        data = self.use_case.generate()

        data_dict = data.model_dump()
        http_response = HttpResponse(status_code=HTTPStatus.OK, body={'result': data_dict})

        return http_response

