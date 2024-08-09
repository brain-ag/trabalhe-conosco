from app.api.v1.schemas.add_producer_schema import AddProducerSchemaIn
from app.domain.dtos.update_rural_producer_confirmation_dto import UpdateRuralProducerConfirmationDto
from pydantic import BaseModel


class UpdateProducerSchemaIn(AddProducerSchemaIn):
    pass


class UpdateProducerSchemaOut(BaseModel):
    result: UpdateRuralProducerConfirmationDto
