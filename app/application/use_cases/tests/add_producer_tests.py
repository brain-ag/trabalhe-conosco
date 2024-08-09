from unittest.mock import Mock

import pytest

from app.application.interfaces.area_size_validator_interface import AreaSizeValidatorInterface
from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface
from app.application.use_cases.add_producer import AddProducer
from app.domain.dtos.add_rural_producer_confirmation_dto import AddRuralProducerConfirmationDto
from app.domain.entities.rural_producer import RuralProducer


@pytest.fixture
def rural_producer_repository():
    return Mock(spec=RuralProducerRepositoryInterface)


@pytest.fixture
def area_size_validator():
    return Mock(spec=AreaSizeValidatorInterface)


@pytest.fixture
def add_producer_use_case(rural_producer_repository, area_size_validator):
    return AddProducer(rural_producer_repository=rural_producer_repository,
                       area_size_validator=area_size_validator)


def test_add_producer_success(add_producer_use_case, rural_producer_repository, area_size_validator):
    producer = RuralProducer(
        id=1,
        nome_produtor="Test Producer",
        area_total_hectares=100.0,
        area_vegetacao_hectares=30.0,
        area_agricultavel_hectares=70.0
    )

    producer_saved = RuralProducer(
        id=2,
        nome_produtor="Test Producer",
        area_total_hectares=100.0,
        area_vegetacao_hectares=30.0,
        area_agricultavel_hectares=70.0
    )

    rural_producer_repository.add.return_value = producer_saved

    result = add_producer_use_case.add(producer=producer)

    area_size_validator.validate.assert_called_once_with(
        total_area=100.0,
        vegetation_area=30.0,
        arable_area=70.0
    )
    rural_producer_repository.add.assert_called_once_with(producer=producer)

    assert isinstance(result, AddRuralProducerConfirmationDto)
    assert result.nome_produtor == "Test Producer"
    assert result.area_total_hectares == 100.0
    assert result.area_vegetacao_hectares == 30.0
    assert result.area_agricultavel_hectares == 70.0


def test_add_producer_invalid_area(add_producer_use_case, area_size_validator):
    producer = RuralProducer(
        id=1,
        nome_produtor="Invalid Producer",
        area_total_hectares=100.0,
        area_vegetacao_hectares=120.0,
        area_agricultavel_hectares=70.0
    )

    area_size_validator.validate.side_effect = ValueError("Invalid area sizes")

    with pytest.raises(ValueError, match="Invalid area sizes"):
        add_producer_use_case.add(producer=producer)

    area_size_validator.validate.assert_called_once_with(
        total_area=100.0,
        vegetation_area=120.0,
        arable_area=70.0
    )

    add_producer_use_case.rural_producer_repository.add.assert_not_called()
