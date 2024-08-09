from http import HTTPStatus
from unittest.mock import Mock
import pytest
from app.domain.dtos.update_rural_producer_confirmation_dto import UpdateRuralProducerConfirmationDto
from app.domain.use_cases.update_producer import UpdateProducer
from app.presentation.controllers.update_producer_controller import UpdateProducerController
from app.presentation.http_types import HttpRequest


@pytest.fixture
def update_producer_use_case():
    return Mock(spec=UpdateProducer)


@pytest.fixture
def controller(update_producer_use_case):
    return UpdateProducerController(use_case=update_producer_use_case)


def test_handle_success(controller, update_producer_use_case):
    # Dados de entrada para o produtor
    producer_data = {
        "documento_tipo": "CPF",
        "documento_numero": "26030008021",
        "nome_produtor": "Updated Producer",
        "nome_fazenda": "Updated Fazenda",
        "cidade": "Updated City",
        "estado": "UC",
        "area_total_hectares": 200.0,
        "area_agricultavel_hectares": 150.0,
        "area_vegetacao_hectares": 50.0,
        "culturas_plantadas": "Soja"
    }

    # Simulação da resposta do use case
    update_producer_use_case.update.return_value = UpdateRuralProducerConfirmationDto(
        **producer_data
    )

    # Criação da requisição HTTP simulada
    http_request = HttpRequest(body=producer_data, path_params={"documento_numero": "26030008021"})

    # Chamando o método handle do controlador
    http_response = controller.handle(http_request)

    # Verificações
    assert http_response.status_code == HTTPStatus.OK
    assert http_response.body['result'] == producer_data

    update_producer_use_case.update.assert_called_once()
    called_producer = update_producer_use_case.update.call_args[1]['producer']
    called_document_number = update_producer_use_case.update.call_args[1]['document_number']
    assert called_producer.documento_tipo == "CPF"
    assert called_producer.documento_numero == "26030008021"
    assert called_producer.nome_produtor == "Updated Producer"
    assert called_producer.nome_fazenda == "Updated Fazenda"
    assert called_producer.cidade == "Updated City"
    assert called_producer.estado == "UC"
    assert called_producer.area_total_hectares == 200.0
    assert called_producer.area_agricultavel_hectares == 150.0
    assert called_producer.area_vegetacao_hectares == 50.0
    assert called_producer.culturas_plantadas == "Soja"
    assert called_document_number == "26030008021"
