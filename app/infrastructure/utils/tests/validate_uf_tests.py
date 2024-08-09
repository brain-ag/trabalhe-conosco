from app.infrastructure.utils.validators import validate_uf


def test_valid_uf():
    brazilian_states = (
        'AC',  # Acre
        'AL',  # Alagoas
        'AP',  # Amapá
        'AM',  # Amazonas
        'BA',  # Bahia
        'CE',  # Ceará
        'DF',  # Distrito Federal
        'ES',  # Espírito Santo
        'GO',  # Goiás
        'MA',  # Maranhão
        'MT',  # Mato Grosso
        'MS',  # Mato Grosso do Sul
        'MG',  # Minas Gerais
        'PA',  # Pará
        'PB',  # Paraíba
        'PR',  # Paraná
        'PE',  # Pernambuco
        'PI',  # Piauí
        'RJ',  # Rio de Janeiro
        'RN',  # Rio Grande do Norte
        'RS',  # Rio Grande do Sul
        'RO',  # Rondônia
        'RR',  # Roraima
        'SC',  # Santa Catarina
        'SP',  # São Paulo
        'SE',  # Sergipe
        'TO'  # Tocantins
    )

    for uf in brazilian_states:
        validate_uf(uf)


def test_invalid_uf():
    uf = "BF"

    assert not validate_uf(uf)

