from app.domain.dtos.dashboard_dto import DashboardDto
from pydantic import BaseModel


class DashboardSchemaOut(BaseModel):
    result: DashboardDto

