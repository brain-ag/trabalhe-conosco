from http import HTTPStatus

from ninja import Router

from app.api.v1.schemas.error_schema import UniqueError, UnprocessableEntityError

from app.errors.error_handler import ErrorHandler
from app.infrastructure.framework.django.adapters.django_request_adapter import DjangoRequestAdapter
from app.infrastructure.services.logging import Logging

from app.api.v1.schemas.add_producer_schema import AddProducerSchemaOut, AddProducerSchemaIn

from app.api.v1.composers.add_producer_composer import AddRuralProducerComposer

logging = Logging()


router = Router(tags=['Produtor Rural'])


@router.post(
    'add',
    response={
        HTTPStatus.OK: AddProducerSchemaOut,
        HTTPStatus.BAD_REQUEST: UniqueError,
        HTTPStatus.INTERNAL_SERVER_ERROR: UniqueError,
        HTTPStatus.UNPROCESSABLE_ENTITY: UnprocessableEntityError,
        HTTPStatus.CONFLICT: UniqueError,
        HTTPStatus.NOT_FOUND: UniqueError,
    },
)
def add(request, add_producer_schema_in: AddProducerSchemaIn):

    try:
        controller = AddRuralProducerComposer().compose()
        http_response = DjangoRequestAdapter().adapt(request=request, controller=controller)
    except Exception as e:
        print(e)
        http_response = ErrorHandler(logging=logging).handle_errors(e)

    return http_response.status_code, http_response.body


