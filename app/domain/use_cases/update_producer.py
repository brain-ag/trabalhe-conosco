from abc import ABC, abstractmethod
from app.domain.entities.rural_producer import RuralProducer
from app.domain.dtos.update_rural_producer_confirmation_dto import UpdateRuralProducerConfirmationDto


class UpdateProducer(ABC):

    @abstractmethod
    def update(self, producer: RuralProducer,
               document_number: str) -> UpdateRuralProducerConfirmationDto:
        pass
