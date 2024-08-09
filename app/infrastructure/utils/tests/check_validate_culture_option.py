from app.infrastructure.utils.validators import validate_culture_option


def test_valid_culture_option():
    culture_option = (
        'soja',
        'algodao',
        'algodão'
    )

    for c in culture_option:
        validate_culture_option(c)


def test_invalid_culture_option():
    culture_option = "INVALID"

    assert not validate_culture_option(culture_option)

