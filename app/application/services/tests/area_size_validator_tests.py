import pytest
from app.errors.types.http_bad_request import HttpBadRequestError
from app.application.services.area_size_validator import AreaSizeValidator


def test_validate_area_correct():
    validator = AreaSizeValidator()
    validator.validate(100.0, 40.0, 50.0)


def test_validate_area_incorrect():
    validator = AreaSizeValidator()
    with pytest.raises(HttpBadRequestError) as exc_info:
        validator.validate(100.0, 60.0, 50.0)
    assert str(exc_info.value) == "Área vegetação + área Agricultável não pode ser maior que área total"


def test_validate_area_edge_case():
    validator = AreaSizeValidator()
    try:
        validator.validate(100.0, 50.0, 50.0)
    except HttpBadRequestError:
        pytest.fail("Unexpected HttpBadRequestError")
