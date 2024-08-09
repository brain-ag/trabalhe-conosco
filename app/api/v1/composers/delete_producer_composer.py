from typing import Any
from app.presentation.controllers.delete_producer_controller import DeleteProducerController
from app.application.use_cases.delete_producer import DeleteProducer
from app.application.services.area_size_validator import AreaSizeValidator
from app.infrastructure.db.repositories.rural_producer_repository import RuralProducerRepository


class DeleteRuralProducerComposer:
    @staticmethod
    def compose() -> Any:
        rural_producer_repository = RuralProducerRepository()
        delete_producer = DeleteProducer(rural_producer_repository=rural_producer_repository)
        delete_producer_controller = DeleteProducerController(use_case=delete_producer)
        return delete_producer_controller
