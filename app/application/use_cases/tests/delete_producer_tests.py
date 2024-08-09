from unittest.mock import Mock
import pytest
from app.application.use_cases.delete_producer import DeleteProducer
from app.domain.dtos.delete_rural_producer_confirmation_dto import DeleteRuralProducerConfirmationDto
from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface


@pytest.fixture
def rural_producer_repository():
    return Mock(spec=RuralProducerRepositoryInterface)


@pytest.fixture
def delete_producer_use_case(rural_producer_repository):
    return DeleteProducer(rural_producer_repository=rural_producer_repository)


def test_delete_producer_success(delete_producer_use_case, rural_producer_repository):
    document_number = "12345678901"

    result = delete_producer_use_case.delete(document_number=document_number)

    rural_producer_repository.delete.assert_called_once_with(document_number=document_number)
    assert isinstance(result, DeleteRuralProducerConfirmationDto)
    assert result.message is True
