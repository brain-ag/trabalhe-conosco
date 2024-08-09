from http import HTTPStatus


class HTTPProcessWithoutPartsError(Exception):
    """Exceção levantada quando um processo não contém partes."""
    def __init__(self, message="Processo sem partes nao e permitido"):
        super().__init__(message)
        self.message = message
        self.name = 'ProcessWithoutPartsError'
        self.status_code = HTTPStatus.UNPROCESSABLE_ENTITY
