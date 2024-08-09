import pytest
from pydantic import ValidationError

from app.api.v1.schemas.add_producer_schema import AddProducerSchemaIn


def mock_validate_uf(value):
    return value in ["SP", "RJ", "MG", "ES"]


def mock_validate_person_type(value):
    return value in ["CPF", "CNPJ"]


def mock_validate_culture_option(value):
    return value in ["Soja", "Milho", "Algodao"]


class MockDocumentValidation:
    def document_validation(self, document):
        return len(document) in [11, 14]


# Applying the mocks
validate_uf = mock_validate_uf
validate_person_type = mock_validate_person_type
validate_culture_option = mock_validate_culture_option
DocumentValidation = MockDocumentValidation


# Test cases
def test_valid_rural_producer_schema():
    data = {
        "documento_tipo": "CPF",
        "documento_numero": "757.694.750-05",
        "nome_produtor": "Jose da Silva",
        "nome_fazenda": "Fazenda Boa Vista",
        "cidade": "Campinas",
        "estado": "SP",
        "area_total_hectares": 150.50,
        "area_agricultavel_hectares": 100.25,
        "area_vegetacao_hectares": 50.25,
        "culturas_plantadas": "Soja"
    }
    schema = AddProducerSchemaIn(**data)
    assert schema.documento_tipo == "CPF"
    assert schema.documento_numero == "75769475005"


def test_invalid_document_number():
    data = {
        "documento_tipo": "CPF",
        "documento_numero": "abcde678901",  # Invalid document number
        "nome_produtor": "Jose da Silva",
        "nome_fazenda": "Fazenda Boa Vista",
        "cidade": "Campinas",
        "estado": "SP",
        "area_total_hectares": 150.50,
        "area_agricultavel_hectares": 100.25,
        "area_vegetacao_hectares": 50.25,
        "culturas_plantadas": "Soja"
    }
    with pytest.raises(ValidationError):
        AddProducerSchemaIn(**data)


def test_invalid_uf():
    data = {
        "documento_tipo": "CPF",
        "documento_numero": "12345678901",
        "nome_produtor": "Jose da Silva",
        "nome_fazenda": "Fazenda Boa Vista",
        "cidade": "Campinas",
        "estado": "XY",  # Invalid UF
        "area_total_hectares": 150.50,
        "area_agricultavel_hectares": 100.25,
        "area_vegetacao_hectares": 50.25,
        "culturas_plantadas": "Soja"
    }
    with pytest.raises(ValidationError):
        AddProducerSchemaIn(**data)


def test_invalid_culture_option():
    data = {
        "documento_tipo": "CPF",
        "documento_numero": "12345678901",
        "nome_produtor": "Jose da Silva",
        "nome_fazenda": "Fazenda Boa Vista",
        "cidade": "Campinas",
        "estado": "SP",
        "area_total_hectares": 150.50,
        "area_agricultavel_hectares": 100.25,
        "area_vegetacao_hectares": 50.25,
        "culturas_plantadas": "Trigo"  # Invalid culture option
    }
    with pytest.raises(ValidationError):
        AddProducerSchemaIn(**data)


def test_field_length_validators():
    data = {
        "documento_tipo": "CPF",
        "documento_numero": "12345678901",
        "nome_produtor": "J" * 101,  # Exceeding length
        "nome_fazenda": "Fazenda Boa Vista",
        "cidade": "Campinas",
        "estado": "SP",
        "area_total_hectares": 150.50,
        "area_agricultavel_hectares": 100.25,
        "area_vegetacao_hectares": 50.25,
        "culturas_plantadas": "Soja"
    }
    with pytest.raises(ValidationError):
        AddProducerSchemaIn(**data)
