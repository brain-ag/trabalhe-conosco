from app.domain.use_cases.update_producer import UpdateProducer
from app.presentation.http_types import HttpRequest, HttpResponse
from app.presentation.interfaces.controller_interface import ControllerInterface
from app.domain.entities.rural_producer import RuralProducer


from http import HTTPStatus
from app.infrastructure.utils.validators import DocumentValidation
from app.errors.types.http_bad_request import HttpBadRequestError


class UpdateProducerController(ControllerInterface):

    def __init__(self, use_case: UpdateProducer):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        data_in = http_request.body
        document_number = http_request.path_params.get("documento_numero")
        document_number = document_number.replace(".", "").replace("-", "").replace("/", "")
        if not DocumentValidation().document_validation(document=document_number):
            raise HttpBadRequestError("Documento Inválido")

        producer = RuralProducer(**data_in)

        data = self.use_case.update(producer=producer,
                                    document_number=document_number)

        data_dict = data.model_dump()
        http_response = HttpResponse(status_code=HTTPStatus.OK, body={'result': data_dict})

        return http_response
