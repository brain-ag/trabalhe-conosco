import unittest
from app.errors.error_handler import ErrorHandler
import uuid
from app.errors.types import HttpBadRequestError, HttpNotFoundError, HttpBadApiRequestError, \
    HttpUnprocessableEntityError
from http import HTTPStatus
from unittest.mock import patch
from app.errors.interfaces.logging_interface import LoggingInterface


class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.logging = unittest.mock.MagicMock(spec=LoggingInterface)
        self.logging.inform.return_value = uuid.UUID('12345678-1234-5678-1234-567812345678')
        self.error_handler = ErrorHandler(self.logging)

    @patch('uuid.uuid4', return_value=uuid.UUID('12345678-1234-5678-1234-567812345678'))
    def test_handle_errors_bad_request(self, mock_uuid):
        error = HttpBadRequestError('Bad Request Error')
        response = self.error_handler.handle_errors(error)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.body, {
            'type': 'BadRequest',
            'error_uuid': [uuid.UUID('12345678-1234-5678-1234-567812345678')],
            'message': 'Bad Request Error'
        })
        self.logging.inform.assert_called_once_with(error=error)

    @patch('uuid.uuid4', return_value=uuid.UUID('12345678-1234-5678-1234-567812345678'))
    def test_handle_errors_not_found(self, mock_uuid):
        error = HttpNotFoundError('Not Found Error')
        response = self.error_handler.handle_errors(error)
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        self.assertEqual(response.body, {
            'type': 'NotFound',
            'error_uuid': [uuid.UUID('12345678-1234-5678-1234-567812345678')],
            'message': 'Not Found Error'
        })
        self.logging.inform.assert_called_once_with(error=error)

    @patch('uuid.uuid4', return_value=uuid.UUID('12345678-1234-5678-1234-567812345678'))
    def test_handle_errors_bad_api_request(self, mock_uuid):
        error = HttpBadApiRequestError('Bad API Request Error', [])
        response = self.error_handler.handle_errors(error)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
        self.assertEqual(response.body, {
            'type': 'BadRequest',
            'error_uuid': [uuid.UUID('12345678-1234-5678-1234-567812345678')],
            'message': 'Bad API Request Error'
        })
        self.logging.inform.assert_called_once_with(error=error)

    @patch('uuid.uuid4', return_value=uuid.UUID('12345678-1234-5678-1234-567812345678'))
    def test_handle_errors_unprocessable_entity(self, mock_uuid):
        error = HttpUnprocessableEntityError('Unprocessable Entity Error', [{'field': 'error'}])
        response = self.error_handler.handle_errors(error)
        self.assertEqual(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        self.assertEqual(response.body, {
            'type': 'UnprocessableEntity',
            'error_uuid': [uuid.UUID('12345678-1234-5678-1234-567812345678')],
            'title': 'Unprocessable Entity Error',
            'notifications': [{'field': 'error'}]
        })
        self.logging.inform.assert_called_once_with(error=error)

    @patch('uuid.uuid4', return_value=uuid.UUID('12345678-1234-5678-1234-567812345678'))
    def test_handle_errors_unexpected_error(self, mock_uuid):
        error = Exception('Unexpected Error')
        response = self.error_handler.handle_errors(error)
        self.assertEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)
        self.assertEqual(response.body, {
            'type': 'Internal Server Error',
            'error_uuid': [uuid.UUID('12345678-1234-5678-1234-567812345678')],
            'message': 'Internal Server Error'
        })
        self.logging.inform.assert_called_once_with(error=error)
