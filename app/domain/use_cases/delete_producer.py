from abc import ABC, abstractmethod
from app.domain.dtos.delete_rural_producer_confirmation_dto import DeleteRuralProducerConfirmationDto


class DeleteProducer(ABC):

    @abstractmethod
    def delete(self, document_number: str) -> DeleteRuralProducerConfirmationDto:
        pass
