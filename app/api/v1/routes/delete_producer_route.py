from http import HTTPStatus

from ninja import Router

from app.api.v1.schemas.error_schema import UniqueError, UnprocessableEntityError

from app.errors.error_handler import ErrorHandler
from app.infrastructure.framework.django.adapters.django_request_adapter import DjangoRequestAdapter
from app.infrastructure.services.logging import Logging

from app.api.v1.schemas.delete_producer_schema import DeleteProducerSchemaOut

from app.api.v1.composers.delete_producer_composer import DeleteRuralProducerComposer

logging = Logging()


router = Router(tags=['Produtor Rural'])


@router.delete(
    'delete/{documento_numero}',
    response={
        HTTPStatus.OK: DeleteProducerSchemaOut,
        HTTPStatus.BAD_REQUEST: UniqueError,
        HTTPStatus.INTERNAL_SERVER_ERROR: UniqueError,
        HTTPStatus.UNPROCESSABLE_ENTITY: UnprocessableEntityError,
        HTTPStatus.CONFLICT: UniqueError,
        HTTPStatus.NOT_FOUND: UniqueError,
    },
)
def delete(request, documento_numero: str):

    try:
        controller = DeleteRuralProducerComposer().compose()
        http_response = DjangoRequestAdapter().adapt(request=request, controller=controller)
    except Exception as e:
        print(e)
        http_response = ErrorHandler(logging=logging).handle_errors(e)

    return http_response.status_code, http_response.body


