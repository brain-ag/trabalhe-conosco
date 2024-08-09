from abc import abstractmethod, ABC
from uuid import UUID


class LoggingInterface(ABC):
    """Classe abstrata para o serviço de logging"""

    @staticmethod
    @abstractmethod
    def inform(error: Exception) -> UUID:

        """Método que informa o erro ao logging, recebe devolve o uuid que a biblioteca de loggining tem que prover"""

        pass

