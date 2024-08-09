from typing import Any
from app.presentation.controllers.update_producer_controller import UpdateProducerController
from app.application.use_cases.update_producer import UpdateProducer
from app.application.services.area_size_validator import AreaSizeValidator
from app.infrastructure.db.repositories.rural_producer_repository import RuralProducerRepository


class UpdateRuralProducerComposer:
    @staticmethod
    def compose() -> Any:
        rural_producer_repository = RuralProducerRepository()
        area_size_validator = AreaSizeValidator()
        update_producer = UpdateProducer(area_size_validator=area_size_validator,
                                         rural_producer_repository=rural_producer_repository)
        update_producer_controller = UpdateProducerController(use_case=update_producer)
        return update_producer_controller
