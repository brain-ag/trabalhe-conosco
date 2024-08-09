from app.domain.use_cases.add_producer import AddProducer
from app.presentation.http_types import HttpRequest, HttpResponse
from app.presentation.interfaces.controller_interface import ControllerInterface
from app.domain.entities.rural_producer import RuralProducer


from http import HTTPStatus


class AddProducerController(ControllerInterface):

    def __init__(self, use_case: AddProducer):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        data_in = http_request.body

        producer = RuralProducer(**data_in)

        data = self.use_case.add(producer=producer)

        data_dict = data.model_dump()
        http_response = HttpResponse(status_code=HTTPStatus.OK, body={'result': data_dict})

        return http_response
