import pytest
from app.infrastructure.utils.validators import ValidateCheckDigit

validate_check_digit = ValidateCheckDigit()


# Testes para validação de dígitos verificadores de processos
@pytest.mark.parametrize("process_number, expected", [
    ("1000880-50.2023.4.01.3606", True),
    ("1000880-50.2023.4.01.3604", False),
    ("0000002-20.2013.8.09.0001", False),
    ("0000002-21.s023.8.09.0001", False),
])
def test_validate_check_digit(process_number, expected):
    assert validate_check_digit.validate(process_number) == expected


