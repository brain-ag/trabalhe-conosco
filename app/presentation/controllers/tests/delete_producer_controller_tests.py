from http import HTTPStatus
from unittest.mock import Mock, patch
import pytest
from app.domain.use_cases.delete_producer import DeleteProducer
from app.domain.dtos.delete_rural_producer_confirmation_dto import DeleteRuralProducerConfirmationDto
from app.presentation.controllers.delete_producer_controller import DeleteProducerController
from app.presentation.http_types import HttpRequest
from app.errors.types.http_bad_request import HttpBadRequestError
from app.infrastructure.utils.validators import DocumentValidation


@pytest.fixture
def delete_producer_use_case():
    return Mock(spec=DeleteProducer)


@pytest.fixture
def controller(delete_producer_use_case):
    return DeleteProducerController(use_case=delete_producer_use_case)


def test_handle_success(controller, delete_producer_use_case):
    document_number = "123.456.789-01"
    clean_document_number = "12345678901"

    delete_producer_use_case.delete.return_value = DeleteRuralProducerConfirmationDto(message=True)

    http_request = HttpRequest(path_params={"documento_numero": document_number})

    with patch.object(DocumentValidation, 'document_validation', return_value=True):
        http_response = controller.handle(http_request)

    assert http_response.status_code == HTTPStatus.OK
    assert http_response.body['result']['message'] is True

    delete_producer_use_case.delete.assert_called_once_with(document_number=clean_document_number)


def test_handle_invalid_document(controller):
    document_number = "invalid-document"

    http_request = HttpRequest(path_params={"documento_numero": document_number})

    with patch.object(DocumentValidation, 'document_validation', return_value=False):
        with pytest.raises(HttpBadRequestError, match="Documento Inválido"):
            controller.handle(http_request)
