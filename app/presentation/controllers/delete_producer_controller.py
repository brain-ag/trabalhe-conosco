from app.domain.use_cases.delete_producer import DeleteProducer
from app.presentation.http_types import HttpRequest, HttpResponse
from app.presentation.interfaces.controller_interface import ControllerInterface


from http import HTTPStatus
from app.infrastructure.utils.validators import DocumentValidation
from app.errors.types.http_bad_request import HttpBadRequestError


class DeleteProducerController(ControllerInterface):

    def __init__(self, use_case: DeleteProducer):
        self.use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        document_number = http_request.path_params.get("documento_numero")
        document_number = document_number.replace(".", "").replace("-", "").replace("/", "")
        if not DocumentValidation().document_validation(document=document_number):
            raise HttpBadRequestError("Documento Inválido")

        data = self.use_case.delete(document_number=document_number)

        data_dict = data.model_dump()
        http_response = HttpResponse(status_code=HTTPStatus.OK, body={'result': data_dict})

        return http_response
