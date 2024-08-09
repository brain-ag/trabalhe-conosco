from abc import ABC, abstractmethod


class AreaSizeValidatorInterface(ABC):

    @abstractmethod
    def validate(self, total_area: float, vegetation_area: float, arable_area: float):
        pass