from app.errors.interfaces.logging_interface import LoggingInterface
from uuid import UUID


class Logging(LoggingInterface):
    """Classe que trabalha como respotitorio pra biblioteca de Logginig que será utilizada.
    Espécia de adaptador. Implementa a interface de Logging na camada de erros"""

    @staticmethod
    def inform(error: Exception) -> UUID:
        # implementar chamadas da biblioteca de logginig aqui
        pass
