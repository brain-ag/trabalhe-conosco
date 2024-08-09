from http import HTTPStatus
from unittest.mock import Mock

import pytest

from app.domain.dtos.add_rural_producer_confirmation_dto import AddRuralProducerConfirmationDto
from app.domain.use_cases.add_producer import AddProducer
from app.presentation.controllers.add_producer_controller import AddProducerController
from app.presentation.http_types import HttpRequest


@pytest.fixture
def add_producer_use_case():
    return Mock(spec=AddProducer)


@pytest.fixture
def controller(add_producer_use_case):
    return AddProducerController(use_case=add_producer_use_case)


def test_handle_success(controller, add_producer_use_case):
    # Dados de entrada para o produtor
    producer_data = {
        "documento_tipo": "CPF",
        "documento_numero": "12345678901",
        "nome_produtor": "Test Producer",
        "nome_fazenda": "Fazenda Teste",
        "cidade": "Test City",
        "estado": "TC",
        "area_total_hectares": 100.0,
        "area_agricultavel_hectares": 70.0,
        "area_vegetacao_hectares": 30.0,
        "culturas_plantadas": "Milho"
    }

    # Simulação da resposta do use case
    add_producer_use_case.add.return_value = AddRuralProducerConfirmationDto(
        **producer_data
    )

    # Criação da requisição HTTP simulada
    http_request = HttpRequest(body=producer_data)

    # Chamando o método handle do controlador
    http_response = controller.handle(http_request)

    # Verificações
    assert http_response.status_code == HTTPStatus.OK
    assert http_response.body['result'] == producer_data

    add_producer_use_case.add.assert_called_once()
    called_producer = add_producer_use_case.add.call_args[1]['producer']
    assert called_producer.documento_tipo == "CPF"
    assert called_producer.documento_numero == "12345678901"
    assert called_producer.nome_produtor == "Test Producer"
    assert called_producer.nome_fazenda == "Fazenda Teste"
    assert called_producer.cidade == "Test City"
    assert called_producer.estado == "TC"
    assert called_producer.area_total_hectares == 100.0
    assert called_producer.area_agricultavel_hectares == 70.0
    assert called_producer.area_vegetacao_hectares == 30.0
    assert called_producer.culturas_plantadas == "Milho"
