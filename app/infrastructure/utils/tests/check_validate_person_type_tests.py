from app.infrastructure.utils.validators import validate_person_type


def test_valid_person_type():
    person_type = (
        'CPF',
        'CNPJ',
    )

    for t in person_type:
        validate_person_type(t)


def test_invalid_person_type():
    person_type = "INVALID"

    assert not validate_person_type(person_type)

