# mypy: disable-error-code=import-untyped

""" Register a new API routers """

from django.http import JsonResponse
from ninja import NinjaAPI
from ninja.errors import ValidationError

from app.errors.error_handler import ErrorHandler
from app.errors.types.http_unprocessable_entity_error import HttpUnprocessableEntityError
from app.infrastructure.services.logging import Logging
from decouple import config

show_swagger = config("SHOW_SWAGGER", cast=bool)
docs_url = None if not show_swagger else "/docs"
api_v1 = NinjaAPI(
    version='1.0.0',
    description='Projeto Agricultor',
    title='Projeto Agricultor',
    docs_url=docs_url
)

logging = Logging()
error_handler = ErrorHandler(logging=logging)


def custom_validation_error_handler(request, exc: ValidationError):
    http_unprocessable_entity_error = HttpUnprocessableEntityError(message="Invalid Entity", errors=exc.errors)
    http_response = error_handler.handle_errors(http_unprocessable_entity_error)
    return JsonResponse(http_response.body, status=http_response.status_code)


# necessario incluir em todos as apis criadas.
api_v1.add_exception_handler(ValidationError, custom_validation_error_handler)

api_v1.add_router('projetoagricultor/', 'app.api.v1.routes.add_producer_route.router')
api_v1.add_router('projetoagricultor/', 'app.api.v1.routes.update_producer_route.router')
api_v1.add_router('projetoagricultor/', 'app.api.v1.routes.delete_producer_route.router')
api_v1.add_router('projetoagricultor/', 'app.api.v1.routes.dashboard_route.router')
