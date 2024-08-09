from unittest.mock import Mock
import pytest
from app.application.interfaces.area_size_validator_interface import AreaSizeValidatorInterface
from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface
from app.application.use_cases.update_producer import UpdateProducer
from app.domain.dtos.update_rural_producer_confirmation_dto import UpdateRuralProducerConfirmationDto
from app.domain.entities.rural_producer import RuralProducer


@pytest.fixture
def rural_producer_repository():
    return Mock(spec=RuralProducerRepositoryInterface)


@pytest.fixture
def area_size_validator():
    return Mock(spec=AreaSizeValidatorInterface)


@pytest.fixture
def update_producer_use_case(rural_producer_repository, area_size_validator):
    return UpdateProducer(rural_producer_repository=rural_producer_repository,
                          area_size_validator=area_size_validator)


def test_update_producer_success(update_producer_use_case, rural_producer_repository, area_size_validator):
    producer = RuralProducer(
        id=1,
        documento_numero="12345678901",
        nome_produtor="Updated Producer",
        area_total_hectares=200.0,
        area_vegetacao_hectares=50.0,
        area_agricultavel_hectares=150.0
    )

    producer_saved = RuralProducer(
        id=1,
        documento_numero="12345678901",
        nome_produtor="Updated Producer",
        area_total_hectares=200.0,
        area_vegetacao_hectares=50.0,
        area_agricultavel_hectares=150.0
    )

    rural_producer_repository.update.return_value = producer_saved

    result = update_producer_use_case.update(producer=producer, document_number="12345678901")

    area_size_validator.validate.assert_called_once_with(
        total_area=200.0,
        vegetation_area=50.0,
        arable_area=150.0
    )
    rural_producer_repository.update.assert_called_once_with(producer=producer, document_number="12345678901")

    assert isinstance(result, UpdateRuralProducerConfirmationDto)
    assert result.nome_produtor == "Updated Producer"
    assert result.area_total_hectares == 200.0
    assert result.area_vegetacao_hectares == 50.0
    assert result.area_agricultavel_hectares == 150.0


def test_update_producer_invalid_area(update_producer_use_case, area_size_validator):
    producer = RuralProducer(
        id=1,
        documento_numero="12345678901",
        nome_produtor="Invalid Producer",
        area_total_hectares=200.0,
        area_vegetacao_hectares=250.0,
        area_agricultavel_hectares=150.0
    )

    area_size_validator.validate.side_effect = ValueError("Invalid area sizes")

    with pytest.raises(ValueError, match="Invalid area sizes"):
        update_producer_use_case.update(producer=producer, document_number="12345678901")

    area_size_validator.validate.assert_called_once_with(
        total_area=200.0,
        vegetation_area=250.0,
        arable_area=150.0
    )

    update_producer_use_case.rural_producer_repository.update.assert_not_called()
