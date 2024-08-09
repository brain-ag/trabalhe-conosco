from app.domain.use_cases.add_producer import AddProducer as AddProducerInterface
from app.domain.entities.rural_producer import RuralProducer
from app.domain.dtos.add_rural_producer_confirmation_dto import AddRuralProducerConfirmationDto
from app.application.interfaces.rural_producer_repository_interface import RuralProducerRepositoryInterface
from app.application.interfaces.area_size_validator_interface import AreaSizeValidatorInterface


class AddProducer(AddProducerInterface):

    def __init__(self, rural_producer_repository: RuralProducerRepositoryInterface,
                area_size_validator: AreaSizeValidatorInterface):
        self.rural_producer_repository = rural_producer_repository
        self.area_size_validator = area_size_validator

    def add(self, producer: RuralProducer) -> AddRuralProducerConfirmationDto:

        self.area_size_validator.validate(total_area=float(producer.area_total_hectares),
                                          vegetation_area=float(producer.area_vegetacao_hectares),
                                          arable_area=float(producer.area_agricultavel_hectares))

        producer_saved = self.rural_producer_repository.add(producer=producer)

        return AddRuralProducerConfirmationDto(**producer_saved.model_dump(exclude={'id'}))
