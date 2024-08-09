import pytest
from app.infrastructure.utils.validators import DocumentValidation

# Instâncias das classes de validação
document_validation = DocumentValidation()


# Testes para validação de CPF
@pytest.mark.parametrize("cpf, expected", [
    ("407.701.140-08", True),
    ("661.414.440-59", True),
    ("000.000.000-00", False),
    ("12345678908", False),
    ("04228772229", False),
])
def test_validate_cpf(cpf, expected):
    assert document_validation.validate_cpf(cpf) == expected


# Testes para validação de CNPJ
@pytest.mark.parametrize("cnpj, expected", [
    ("80.112.921/0001-85", True),
    ("90.350.632/0001-78", True),
    ("00.000.000/0000-00", False),
    ("90.350.632/0001-73", False),
    ("79276140000147", True),
])
def test_validate_cnpj(cnpj, expected):
    assert document_validation.validate_cnpj(cnpj) == expected


# Testes para validação de documentos em geral
@pytest.mark.parametrize("document, expected", [
    ("119.646.890-74", True),
    ("119.646.890-73", False),
    ("07.275.328/0001-61", False),
    ("07.275.328/0001-60", True),
    ("", False),
    (None, False),
])
def test_document_validation(document, expected):
    assert document_validation.document_validation(document) == expected

