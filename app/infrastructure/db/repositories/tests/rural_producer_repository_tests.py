import pytest
from decimal import Decimal
from app.domain.entities.rural_producer import RuralProducer
from app.infrastructure.framework.django.apps.rural_producer.models import RuralProducer as RuralProducerModel
from app.infrastructure.db.repositories.rural_producer_repository import RuralProducerRepository


@pytest.mark.django_db
def test_add_producer_success():
    producer = RuralProducer(
        documento_tipo="CPF",
        documento_numero="12345678901",
        nome_produtor="Test Producer",
        nome_fazenda="Fazenda Teste",
        cidade="Test City",
        estado="TC",
        area_total_hectares=Decimal("100.00"),
        area_agricultavel_hectares=Decimal("70.00"),
        area_vegetacao_hectares=Decimal("30.00"),
        culturas_plantadas="Milho"
    )

    repository = RuralProducerRepository()
    result = repository.add(producer=producer)

    assert result.documento_tipo == "CPF"
    assert result.documento_numero == "12345678901"
    assert result.nome_produtor == "Test Producer"
    assert result.nome_fazenda == "Fazenda Teste"
    assert result.cidade == "Test City"
    assert result.estado == "TC"
    assert result.area_total_hectares == Decimal("100.00")
    assert result.area_agricultavel_hectares == Decimal("70.00")
    assert result.area_vegetacao_hectares == Decimal("30.00")
    assert result.culturas_plantadas == "Milho"

    saved_producer = RuralProducerModel.objects.get(id=result.id)
    assert saved_producer.documento_tipo == "CPF"
    assert saved_producer.documento_numero == "12345678901"
    assert saved_producer.nome_produtor == "Test Producer"
    assert saved_producer.nome_fazenda == "Fazenda Teste"
    assert saved_producer.cidade == "Test City"
    assert saved_producer.estado == "TC"
    assert saved_producer.area_total_hectares == Decimal("100.00")
    assert saved_producer.area_agricultavel_hectares == Decimal("70.00")
    assert saved_producer.area_vegetacao_hectares == Decimal("30.00")
    assert saved_producer.culturas_plantadas == "Milho"


@pytest.mark.django_db
def test_update_producer_success():
    producer = RuralProducerModel.objects.create(
        documento_tipo="CPF",
        documento_numero="12345678901",
        nome_produtor="Test Producer",
        nome_fazenda="Fazenda Teste",
        cidade="Test City",
        estado="TC",
        area_total_hectares=Decimal("100.00"),
        area_agricultavel_hectares=Decimal("70.00"),
        area_vegetacao_hectares=Decimal("30.00"),
        culturas_plantadas="Milho"
    )

    updated_producer = RuralProducer(
        id=producer.id,
        documento_tipo="CNPJ",
        documento_numero="98765432100",
        nome_produtor="Updated Producer",
        nome_fazenda="Updated Fazenda",
        cidade="Updated City",
        estado="UC",
        area_total_hectares=Decimal("200.00"),
        area_agricultavel_hectares=Decimal("150.00"),
        area_vegetacao_hectares=Decimal("50.00"),
        culturas_plantadas="Soja"
    )

    repository = RuralProducerRepository()
    result = repository.update(producer=updated_producer, document_number="12345678901")

    assert result.documento_tipo == "CNPJ"
    assert result.documento_numero == "98765432100"
    assert result.nome_produtor == "Updated Producer"
    assert result.nome_fazenda == "Updated Fazenda"
    assert result.cidade == "Updated City"
    assert result.estado == "UC"
    assert result.area_total_hectares == Decimal("200.00")
    assert result.area_agricultavel_hectares == Decimal("150.00")
    assert result.area_vegetacao_hectares == Decimal("50.00")
    assert result.culturas_plantadas == "Soja"

    saved_producer = RuralProducerModel.objects.get(id=result.id)
    assert saved_producer.documento_tipo == "CNPJ"
    assert saved_producer.documento_numero == "98765432100"
    assert saved_producer.nome_produtor == "Updated Producer"
    assert saved_producer.nome_fazenda == "Updated Fazenda"
    assert saved_producer.cidade == "Updated City"
    assert saved_producer.estado == "UC"
    assert saved_producer.area_total_hectares == Decimal("200.00")
    assert saved_producer.area_agricultavel_hectares == Decimal("150.00")
    assert saved_producer.area_vegetacao_hectares == Decimal("50.00")
    assert saved_producer.culturas_plantadas == "Soja"


@pytest.mark.django_db
def test_delete_producer_success():
    producer = RuralProducerModel.objects.create(
        documento_tipo="CPF",
        documento_numero="12345678901",
        nome_produtor="Test Producer",
        nome_fazenda="Fazenda Teste",
        cidade="Test City",
        estado="TC",
        area_total_hectares=Decimal("100.00"),
        area_agricultavel_hectares=Decimal("70.00"),
        area_vegetacao_hectares=Decimal("30.00"),
        culturas_plantadas="Milho"
    )

    repository = RuralProducerRepository()
    repository.delete(document_number="12345678901")

    with pytest.raises(RuralProducerModel.DoesNotExist):
        RuralProducerModel.objects.get(documento_numero="12345678901")


@pytest.mark.django_db
def test_total_of_farms_success():
    RuralProducerModel.objects.bulk_create([
        RuralProducerModel(
            documento_tipo="CPF",
            documento_numero=f"1234567890{i}",
            nome_produtor=f"Test Producer {i}",
            nome_fazenda=f"Fazenda Teste {i}",
            cidade=f"Test City {i}",
            estado="TC",
            area_total_hectares=Decimal("100.00"),
            area_agricultavel_hectares=Decimal("70.00"),
            area_vegetacao_hectares=Decimal("30.00"),
            culturas_plantadas="Milho"
        ) for i in range(3)
    ])

    repository = RuralProducerRepository()
    total_farms = repository.total_of_farms()

    assert total_farms == 3


@pytest.mark.django_db
def test_total_of_hectares_success():
    RuralProducerModel.objects.bulk_create([
        RuralProducerModel(
            documento_tipo="CPF",
            documento_numero=f"1234567890{i}",
            nome_produtor=f"Test Producer {i}",
            nome_fazenda=f"Fazenda Teste {i}",
            cidade=f"Test City {i}",
            estado="TC",
            area_total_hectares=Decimal("100.00"),
            area_agricultavel_hectares=Decimal("70.00"),
            area_vegetacao_hectares=Decimal("30.00"),
            culturas_plantadas="Milho"
        ) for i in range(3)
    ])

    repository = RuralProducerRepository()
    total_hectares = repository.total_of_hectares()

    assert total_hectares == 300.00


@pytest.mark.django_db
def test_area_by_state_success():
    RuralProducerModel.objects.bulk_create([
        RuralProducerModel(
            documento_tipo="CPF",
            documento_numero=f"1234567890{i}",
            nome_produtor=f"Test Producer {i}",
            nome_fazenda=f"Fazenda Teste {i}",
            cidade=f"Test City {i}",
            estado="TC" if i % 2 == 0 else "UC",
            area_total_hectares=Decimal("100.00"),
            area_agricultavel_hectares=Decimal("70.00"),
            area_vegetacao_hectares=Decimal("30.00"),
            culturas_plantadas="Milho"
        ) for i in range(4)
    ])

    repository = RuralProducerRepository()
    areas_by_state = repository.area_by_state()

    assert len(areas_by_state) == 2
    assert areas_by_state[0].estado == "TC"
    assert areas_by_state[0].total == 200.00
    assert areas_by_state[1].estado == "UC"
    assert areas_by_state[1].total == 200.00


@pytest.mark.django_db
def test_area_by_culture_success():
    RuralProducerModel.objects.bulk_create([
        RuralProducerModel(
            documento_tipo="CPF",
            documento_numero=f"1234567890{i}",
            nome_produtor=f"Test Producer {i}",
            nome_fazenda=f"Fazenda Teste {i}",
            cidade=f"Test City {i}",
            estado="TC",
            area_total_hectares=Decimal("100.00"),
            area_agricultavel_hectares=Decimal("70.00"),
            area_vegetacao_hectares=Decimal("30.00"),
            culturas_plantadas="Milho" if i % 2 == 0 else "Soja"
        ) for i in range(4)
    ])

    repository = RuralProducerRepository()
    areas_by_culture = repository.area_by_culture()

    assert len(areas_by_culture) == 2
    assert areas_by_culture[0].cultura == "Soja"
    assert areas_by_culture[0].total == 200.00
    assert areas_by_culture[1].cultura == "Milho"
    assert areas_by_culture[1].total == 200.00


@pytest.mark.django_db
def test_soil_use_success():
    RuralProducerModel.objects.bulk_create([
        RuralProducerModel(
            documento_tipo="CPF",
            documento_numero=f"1234567890{i}",
            nome_produtor=f"Test Producer {i}",
            nome_fazenda=f"Fazenda Teste {i}",
            cidade=f"Test City {i}",
            estado="TC",
            area_total_hectares=Decimal("100.00"),
            area_agricultavel_hectares=Decimal("70.00"),
            area_vegetacao_hectares=Decimal("30.00"),
            culturas_plantadas="Milho"
        ) for i in range(3)
    ])

    repository = RuralProducerRepository()
    soil_use = repository.soil_use()

    assert soil_use.total_agricultavel == 210.00
    assert soil_use.total_vegetacao == 90.00
