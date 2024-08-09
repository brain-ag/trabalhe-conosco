# mypy: disable-error-code=valid-type

""" Module Http Request """

from dataclasses import dataclass


@dataclass
class HttpRequest:
    """ Class Http Request """
    headers: any = None
    body: dict | None = None
    query_params: any = None
    url: any = None
    ipv4: any = None
    path_params: any = None
    files: any = None
