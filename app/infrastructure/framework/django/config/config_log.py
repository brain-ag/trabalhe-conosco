# mypy: disable-error-code=import-untyped

""" Configuration log in Dynatrace """

import json
from logging import INFO, Formatter, Handler, StreamHandler, getLogger
from logging.handlers import SysLogHandler
from sys import platform

import requests
from decouple import config

PROJETO = config('PROJETO')
DYNATRACE_LOGS = config('DYNATRACE_LOGS', default=False, cast=bool)


class ExternalServiceHandler(Handler):
    """Handler for external services"""

    def __init__(self, url, token):
        super().__init__()
        self.url = url
        self.token = token

    def emit(self, record):
        log_entry = self.format(record)
        payload = json.loads(log_entry)

        payload.update({'projeto': PROJETO})
        payload.update({'message': f'{PROJETO}: {record.message}'})

        headers = {'Authorization': f'Api-Token {self.token}', 'Content-Type': 'application/json'}

        requests.post(self.url, json=payload, headers=headers)


formatter = Formatter(
    f'{PROJETO} %(levelname)s: file:%(pathname)s/%(filename)s %(funcName)s:line:%(lineno)s: %(message)s'
)

json_formatter = Formatter(
    '{ "timestamp": "%(asctime)s", "severity": "%(levelname)s", "file": "file:%(pathname)s %(filename)s %(funcName)s line:%(lineno)s" }'  # noqa E501
)


def config_log():
    """Configure logging"""
    logger = getLogger('root')

    logger.setLevel(INFO)

    console = StreamHandler()
    console.setLevel(INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)

    if platform == 'linux':
        syslog = SysLogHandler()
        syslog.setLevel(INFO)
        syslog.setFormatter(formatter)
        logger.addHandler(syslog)

    if DYNATRACE_LOGS:
        external_service = ExternalServiceHandler(url=config('DYNATRACE_URL'), token=config('DYNATRACE_TOKEN'))
        external_service.setLevel(INFO)
        external_service.setFormatter(json_formatter)

        logger.addHandler(external_service)
