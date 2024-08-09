from app.application.interfaces.area_size_validator_interface import AreaSizeValidatorInterface
from app.errors.types.http_bad_request import HttpBadRequestError


class AreaSizeValidator(AreaSizeValidatorInterface):

    def validate(self, total_area: float, vegetation_area: float, arable_area: float):
        if vegetation_area + arable_area > total_area:
            raise HttpBadRequestError("Área vegetação + área Agricultável não pode ser maior que área total")

