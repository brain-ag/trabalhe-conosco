from app.infrastructure.utils.remove_accents import remove_accents


def test_remover_acentos():
    assert remove_accents("Olá, mundo! Como você está?") == "Ola, mundo! Como voce esta?"
    assert remove_accents("Café") == "Cafe"
    assert remove_accents("Pão de açúcar") == "Pao de acucar"
    assert remove_accents("ação") == "acao"
    assert remove_accents("123") == "123"
    assert remove_accents("") == ""
