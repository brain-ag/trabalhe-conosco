from app.domain.dtos.add_rural_producer_confirmation_dto import AddRuralProducerConfirmationDto
from pydantic import BaseModel


class DeleteRuralProducerConfirmationDto(BaseModel):
    message: bool
