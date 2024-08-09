import pytest
from unittest.mock import Mock
from http import HTTPStatus
from app.domain.use_cases.dashboard import Dashboard
from app.presentation.http_types import HttpRequest, HttpResponse
from app.presentation.controllers.dashboard_controller import DashboardController
from app.domain.dtos.dashboard_dto import DashboardDto, AreaByStatePizza, AreaByCulturePizza, SoilUsePizza


@pytest.fixture
def mock_use_case():
    return Mock(spec=Dashboard)


@pytest.fixture
def controller(mock_use_case):
    return DashboardController(use_case=mock_use_case)


def test_handle(controller, mock_use_case):
    mock_use_case.generate.return_value = DashboardDto(
        total_fazendas=10,
        total_hectares=500.0,
        grafico_pizza_estado=[
            AreaByStatePizza(estado='SP', porcentagem=40.0),
            AreaByStatePizza(estado='MG', porcentagem=30.0),
            AreaByStatePizza(estado='RJ', porcentagem=30.0),
        ],
        grafico_pizza_cultura=[
            AreaByCulturePizza(cultura='Milho', porcentagem=60.0),
            AreaByCulturePizza(cultura='Soja', porcentagem=40.0),
        ],
        grafico_pizza_uso_solo=SoilUsePizza(
            porcentagem_agricultavel=70.0,
            porcentagem_vegetacao=30.0
        )
    )

    http_request = HttpRequest()

    http_response = controller.handle(http_request)

    # Verificações
    assert http_response.status_code == HTTPStatus.OK
    assert 'result' in http_response.body

    assert http_response.body['result']['total_fazendas'] == 10
    assert http_response.body['result']['total_hectares'] == 500.0
    assert len(http_response.body['result']['grafico_pizza_estado']) == 3
    assert len(http_response.body['result']['grafico_pizza_cultura']) == 2
    assert http_response.body['result']['grafico_pizza_uso_solo']['porcentagem_agricultavel'] == 70.0
    assert http_response.body['result']['grafico_pizza_uso_solo']['porcentagem_vegetacao'] == 30.0
