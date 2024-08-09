from typing import Any
from app.presentation.controllers.dashboard_controller import DashboardController
from app.application.use_cases.dashboard import Dashboard
from app.application.services.area_size_validator import AreaSizeValidator
from app.infrastructure.db.repositories.rural_producer_repository import RuralProducerRepository


class DashboardComposer:
    @staticmethod
    def compose() -> Any:
        rural_producer_repository = RuralProducerRepository()
        dashboard = Dashboard(rural_producer_repository=rural_producer_repository)
        dashboard_controller = DashboardController(use_case=dashboard)
        return dashboard_controller
