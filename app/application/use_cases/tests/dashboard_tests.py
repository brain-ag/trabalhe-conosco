import pytest
from unittest.mock import Mock
from app.application.use_cases.dashboard import Dashboard
from app.domain.dtos.dashboard_dto import (AreaByStatePizza,
                                           AreaByCulturePizza,
                                           SoilUsePizza,
                                           DashboardDto,
                                           SoilUse,
                                           AreaByCulture,
                                           AreaByState)
from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface


@pytest.fixture
def mock_repository():
    return Mock(spec=RuralProducerRepositoryInterface)


@pytest.fixture
def dashboard_use_case(mock_repository):
    return Dashboard(rural_producer_repository=mock_repository)


def test_generate_dashboard(dashboard_use_case, mock_repository):
    mock_repository.total_of_farms.return_value = 10
    mock_repository.total_of_hectares.return_value = 500.0

    mock_repository.area_by_state.return_value = [
        AreaByState(estado='SP', total=200.0),
        AreaByState(estado='MG', total=150.0),
        AreaByState(estado='RJ', total=150.0),
    ]

    mock_repository.area_by_culture.return_value = [
        AreaByCulture(cultura='Milho', total=300.0),
        AreaByCulture(cultura='Soja', total=200.0),
    ]

    mock_repository.soil_use.return_value = SoilUse(
        total_agricultavel=350.0,
        total_vegetacao=150.0
    )

    dashboard_dto = dashboard_use_case.generate()

    assert dashboard_dto.total_fazendas == 10
    assert dashboard_dto.total_hectares == 500.0

    assert len(dashboard_dto.grafico_pizza_estado) == 3
    assert dashboard_dto.grafico_pizza_estado[0].estado == 'SP'
    assert dashboard_dto.grafico_pizza_estado[0].porcentagem == 40.0  # 200/500 * 100
    assert dashboard_dto.grafico_pizza_estado[1].estado == 'MG'
    assert dashboard_dto.grafico_pizza_estado[1].porcentagem == 30.0  # 150/500 * 100
    assert dashboard_dto.grafico_pizza_estado[2].estado == 'RJ'
    assert dashboard_dto.grafico_pizza_estado[2].porcentagem == 30.0  # 150/500 * 100

    assert len(dashboard_dto.grafico_pizza_cultura) == 2
    assert dashboard_dto.grafico_pizza_cultura[0].cultura == 'Milho'
    assert dashboard_dto.grafico_pizza_cultura[0].porcentagem == 60.0  # 300/500 * 100
    assert dashboard_dto.grafico_pizza_cultura[1].cultura == 'Soja'
    assert dashboard_dto.grafico_pizza_cultura[1].porcentagem == 40.0  # 200/500 * 100

    assert dashboard_dto.grafico_pizza_uso_solo.porcentagem_agricultavel == 70.0  # 350/500 * 100
    assert dashboard_dto.grafico_pizza_uso_solo.porcentagem_vegetacao == 30.0  # 150/500 * 100


def test_generate_area_by_state(dashboard_use_case, mock_repository):
    mock_repository.area_by_state.return_value = [
        AreaByState(estado='SP', total=200.0),
        AreaByState(estado='MG', total=150.0),
        AreaByState(estado='RJ', total=150.0),
    ]

    result = dashboard_use_case._generate_area_by_state()

    assert len(result) == 3
    assert result[0].estado == 'SP'
    assert result[0].porcentagem == 40.0  # 200/500 * 100
    assert result[1].estado == 'MG'
    assert result[1].porcentagem == 30.0  # 150/500 * 100
    assert result[2].estado == 'RJ'
    assert result[2].porcentagem == 30.0  # 150/500 * 100


def test_generate_area_by_culture(dashboard_use_case, mock_repository):
    mock_repository.area_by_culture.return_value = [
        AreaByCulture(cultura='Milho', total=300.0),
        AreaByCulture(cultura='Soja', total=200.0),
    ]

    result = dashboard_use_case._generate_area_by_culture()

    assert len(result) == 2
    assert result[0].cultura == 'Milho'
    assert result[0].porcentagem == 60.0  # 300/500 * 100
    assert result[1].cultura == 'Soja'
    assert result[1].porcentagem == 40.0  # 200/500 * 100


def test_generate_soil_use(dashboard_use_case, mock_repository):
    mock_repository.soil_use.return_value = SoilUse(
        total_agricultavel=350.0,
        total_vegetacao=150.0
    )

    result = dashboard_use_case._generate_soil_use()

    assert result.porcentagem_agricultavel == 70.0  # 350/500 * 100
    assert result.porcentagem_vegetacao == 30.0  # 150/500 * 100
