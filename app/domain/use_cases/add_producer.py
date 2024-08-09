from abc import ABC, abstractmethod
from app.domain.entities.rural_producer import RuralProducer
from app.domain.dtos.add_rural_producer_confirmation_dto import AddRuralProducerConfirmationDto


class AddProducer(ABC):

    @abstractmethod
    def add(self, producer: RuralProducer) -> AddRuralProducerConfirmationDto:
        pass
