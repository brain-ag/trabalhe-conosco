from abc import abstractmethod, ABC
from app.domain.dtos.dashboard_dto import DashboardDto


class Dashboard(ABC):

    @abstractmethod
    def generate(self) -> DashboardDto:
        pass