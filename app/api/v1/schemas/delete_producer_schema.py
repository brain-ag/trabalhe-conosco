from app.domain.dtos.delete_rural_producer_confirmation_dto import DeleteRuralProducerConfirmationDto
from pydantic import BaseModel


class DeleteProducerSchemaOut(BaseModel):
    result: DeleteRuralProducerConfirmationDto
