from http import HTTPStatus

from ninja import Router

from app.api.v1.schemas.error_schema import UniqueError, UnprocessableEntityError

from app.errors.error_handler import ErrorHandler
from app.infrastructure.framework.django.adapters.django_request_adapter import DjangoRequestAdapter
from app.infrastructure.services.logging import Logging

from app.api.v1.schemas.update_producer_schema import UpdateProducerSchemaIn, UpdateProducerSchemaOut

from app.api.v1.composers.update_producer_composer import UpdateRuralProducerComposer

logging = Logging()


router = Router(tags=['Produtor Rural'])


@router.put(
    'update/{documento_numero}',
    response={
        HTTPStatus.OK: UpdateProducerSchemaOut,
        HTTPStatus.BAD_REQUEST: UniqueError,
        HTTPStatus.INTERNAL_SERVER_ERROR: UniqueError,
        HTTPStatus.UNPROCESSABLE_ENTITY: UnprocessableEntityError,
        HTTPStatus.CONFLICT: UniqueError,
        HTTPStatus.NOT_FOUND: UniqueError,
    },
)
def update(request, update_producer_schema_in: UpdateProducerSchemaIn, documento_numero: str):

    try:
        controller = UpdateRuralProducerComposer().compose()
        http_response = DjangoRequestAdapter().adapt(request=request, controller=controller)
    except Exception as e:
        print(e)
        http_response = ErrorHandler(logging=logging).handle_errors(e)

    return http_response.status_code, http_response.body


