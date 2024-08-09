from app.domain.use_cases.dashboard import Dashboard as DashboardInterface
from app.domain.dtos.dashboard_dto import DashboardDto, AreaByStatePizza, AreaByCulturePizza, SoilUsePizza
from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface


class Dashboard(DashboardInterface):

    def __init__(self, rural_producer_repository: RuralProducerRepositoryInterface):
        self.rural_producer_repository = rural_producer_repository

    def generate(self) -> DashboardDto:
        dashboard_dto = DashboardDto()

        dashboard_dto.total_fazendas = self.rural_producer_repository.total_of_farms()
        dashboard_dto.total_hectares = self.rural_producer_repository.total_of_hectares()

        dashboard_dto.grafico_pizza_estado = self._generate_area_by_state()
        dashboard_dto.grafico_pizza_cultura = self._generate_area_by_culture()
        dashboard_dto.grafico_pizza_uso_solo = self._generate_soil_use()

        return dashboard_dto

    def _generate_area_by_state(self) -> list[AreaByStatePizza] | None:
        areas_by_state = self.rural_producer_repository.area_by_state()
        if not areas_by_state:
            return

        total_hectares_state = sum(item.total for item in areas_by_state)

        return [
            AreaByStatePizza(
                estado=item.estado,
                porcentagem=(item.total / total_hectares_state) * 100 if total_hectares_state > 0 else 0
            ) for item in areas_by_state
        ]

    def _generate_area_by_culture(self) -> list[AreaByCulturePizza] | None:
        areas_by_culture = self.rural_producer_repository.area_by_culture()

        if not areas_by_culture:
            return

        total_hectares_culture = sum(item.total for item in areas_by_culture)

        return [
            AreaByCulturePizza(
                cultura=item.cultura,
                porcentagem=(item.total / total_hectares_culture) * 100 if total_hectares_culture > 0 else 0
            ) for item in areas_by_culture
        ]

    def _generate_soil_use(self) -> SoilUsePizza | None:
        soil_use = self.rural_producer_repository.soil_use()

        if not soil_use:
            return


        total_soil_use = (soil_use.total_agricultavel or 0) + (soil_use.total_vegetacao or 0)

        return SoilUsePizza(
            porcentagem_agricultavel=(soil_use.total_agricultavel / total_soil_use) * 100 if total_soil_use > 0 else 0,
            porcentagem_vegetacao=(soil_use.total_vegetacao / total_soil_use) * 100 if total_soil_use > 0 else 0
        )
