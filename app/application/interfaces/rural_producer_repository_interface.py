from abc import ABC, abstractmethod
from app.domain.entities.rural_producer import RuralProducer
from app.domain.dtos.dashboard_dto import SoilUse,AreaByState, AreaByCulture
from decimal import Decimal


class RuralProducerRepositoryInterface(ABC):

    @abstractmethod
    def add(self, producer: RuralProducer) -> RuralProducer:
        pass

    @abstractmethod
    def update(self, producer: RuralProducer, document_number: str) -> RuralProducer:
        pass

    @abstractmethod
    def delete(self, document_number: str):
        pass

    @abstractmethod
    def total_of_farms(self) -> int:
        pass

    @abstractmethod
    def total_of_hectares(self) -> Decimal:
        pass

    @abstractmethod
    def area_by_state(self) -> list[AreaByState]:
        pass

    @abstractmethod
    def area_by_culture(self) -> list[AreaByCulture]:
        pass

    @abstractmethod
    def soil_use(self) -> SoilUse:
        pass

