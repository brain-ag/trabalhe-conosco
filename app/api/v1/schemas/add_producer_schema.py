from app.infrastructure.utils.validators import (validate_uf,
                                                 validate_person_type,
                                                 validate_culture_option,
                                                 DocumentValidation)
from app.infrastructure.utils.remove_accents import remove_accents
from pydantic import BaseModel, field_validator, condecimal, model_validator
from app.domain.dtos.add_rural_producer_confirmation_dto import AddRuralProducerConfirmationDto


class AddProducerSchemaIn(BaseModel):
    documento_tipo: str
    documento_numero: str
    nome_produtor: str
    nome_fazenda: str
    cidade: str
    estado: str
    area_total_hectares: condecimal(max_digits=10, decimal_places=2, ge=0)
    area_agricultavel_hectares: condecimal(max_digits=10, decimal_places=2, ge=0)
    area_vegetacao_hectares: condecimal(max_digits=10, decimal_places=2, ge=0)
    culturas_plantadas: str

    @field_validator('documento_numero')
    def validate_document(cls, v):
        v = v.replace(".", "").replace("-", "").replace("/", "")

        if not v.isdigit():
            raise ValueError('Caractere invalido no documento')

        if not DocumentValidation().document_validation(document=v):
            raise ValueError('Documento Invalido')
        return v

    @field_validator('estado')
    def validate_uf(cls, value):
        if validate_uf(value):
            return value
        else:
            raise ValueError(f"UF invalida: {value}")

    @field_validator('documento_tipo')
    def validate_person_type(cls, value):
        if validate_person_type(value):
            return value
        else:
            raise ValueError(f"Invalid person type: {value}")

    @field_validator('culturas_plantadas')
    def validate_culturas_plantadas(cls, value):
        value = remove_accents(value)
        if validate_culture_option(value):
            return value
        else:
            raise ValueError(f"Invalid culture option: {value}")

    @model_validator(mode='before')
    def validate_fields(cls, values):
        documento_tipo = values.get("documento_tipo")
        documento_numero = values.get("documento_numero")
        if documento_tipo.lower() == "cpf":
            if not DocumentValidation().validate_cpf(documento_numero):
                raise ValueError('Documento Invalido')
        else:
            if not DocumentValidation().validate_cnpj(documento_numero):
                raise ValueError('Documento Invalido')

        values["numero_processo"] = documento_numero.replace(".", "").replace("-", "").replace("/", "")

        return values


class AddProducerSchemaOut(BaseModel):
    result: AddRuralProducerConfirmationDto
    