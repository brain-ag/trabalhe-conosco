from http import HTTPStatus


class HTTPUniqueConstraintError(Exception):
    """Exceção levantada quando tento cadastrar numero de processo existente"""
    def __init__(self, message="Número de processo ja cadastrado"):
        super().__init__(message)
        self.message = message
        self.name = 'UniqueConstraintError'
        self.status_code = HTTPStatus.CONFLICT
