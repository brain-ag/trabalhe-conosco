from typing import Any
from app.presentation.controllers.add_producer_controller import AddProducerController
from app.application.use_cases.add_producer import AddProducer
from app.application.services.area_size_validator import AreaSizeValidator
from app.infrastructure.db.repositories.rural_producer_repository import RuralProducerRepository


class AddRuralProducerComposer:
    @staticmethod
    def compose() -> Any:
        rural_producer_repository = RuralProducerRepository()
        area_size_validator = AreaSizeValidator()
        add_producer = AddProducer(area_size_validator=area_size_validator,
                                   rural_producer_repository=rural_producer_repository)
        add_producer_controller = AddProducerController(use_case=add_producer)
        return add_producer_controller
