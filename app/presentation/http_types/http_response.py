""" Module Http Response """

from dataclasses import dataclass


@dataclass
class HttpResponse:
    """ Class Http Response """
    status_code: int
    body: dict | None = None
