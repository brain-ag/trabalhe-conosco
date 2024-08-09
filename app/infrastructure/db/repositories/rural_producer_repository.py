from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface
from app.domain.entities.rural_producer import RuralProducer
from app.infrastructure.framework.django.apps.rural_producer.models import RuralProducer as RuralProducerModel
from app.errors.types import HttpNotFoundError
from django.db.models import Sum
from app.domain.dtos.dashboard_dto import SoilUse, AreaByState, AreaByCulture
from decimal import Decimal


class RuralProducerRepository(RuralProducerRepositoryInterface):

    def add(self, producer: RuralProducer) -> RuralProducer:

        new_producer = RuralProducerModel(**producer.model_dump(exclude={'id'}))
        new_producer.save()

        return RuralProducer.model_validate(new_producer)

    def update(self, producer: RuralProducer, document_number: str) -> RuralProducer:
        producer_model = self.__get_by_document_number(document_number=document_number)

        # permito a edição do numero do documento, so nao permito que o id possa ser atualizado
        for key, value in producer.model_dump(exclude={"id"}).items():
            setattr(producer_model, key, value)

        producer_model.save()

        return RuralProducer.model_validate(producer_model)

    def delete(self, document_number: str):
        producer = self.__get_by_document_number(document_number=document_number)
        producer.delete()

    def total_of_farms(self) -> int:
        print("total", RuralProducerModel.objects.count())
        return RuralProducerModel.objects.count()

    def total_of_hectares(self) -> Decimal:
        return RuralProducerModel.objects.aggregate(total=Sum('area_total_hectares'))['total']

    def area_by_state(self) -> list[AreaByState] | None:
        result = RuralProducerModel.objects.values('estado').annotate(total=Sum('area_total_hectares')).order_by('-total')
        print("Area", result)
        return [AreaByState(estado=item['estado'], total=item['total']) for item in result]

    def area_by_culture(self) -> list[AreaByCulture] | None:
        result = RuralProducerModel.objects.values('culturas_plantadas').annotate(total=Sum('area_total_hectares')).order_by(
            '-total')
        print("Cultura", result)
        return [AreaByCulture(cultura=item['culturas_plantadas'], total=item['total']) for item in result]

    def soil_use(self) -> SoilUse | None:
        result = RuralProducerModel.objects.aggregate(
            total_agricultavel=Sum('area_agricultavel_hectares'),
            total_vegetacao=Sum('area_vegetacao_hectares')
        )
        print("Solo", result)
        return SoilUse(**result)

    @staticmethod
    def __get_by_document_number(document_number: str) -> RuralProducerModel:
        try:
            producer = RuralProducerModel.objects.get(documento_numero=document_number)
            return producer
        except RuralProducerModel.DoesNotExist:
            raise HttpNotFoundError("Produtor não encontrado")


