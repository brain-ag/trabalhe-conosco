from app.domain.use_cases.delete_producer import DeleteProducer as DeleteProducerInterface
from app.domain.dtos.delete_rural_producer_confirmation_dto import DeleteRuralProducerConfirmationDto
from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface


class DeleteProducer(DeleteProducerInterface):

    def __init__(self, rural_producer_repository: RuralProducerRepositoryInterface):
        self.rural_producer_repository = rural_producer_repository

    def delete(self, document_number: str) -> DeleteRuralProducerConfirmationDto:
        self.rural_producer_repository.delete(document_number=document_number)

        return DeleteRuralProducerConfirmationDto(message=True)
