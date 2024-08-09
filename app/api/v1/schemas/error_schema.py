""" Module Schema Error """

from uuid import UUID

from pydantic import BaseModel

from typing import List, Dict, Any


class UniqueError(BaseModel):
    """ Class Unique Error """
    type: str
    error_uuid: list[UUID]
    message: str


class UnprocessableEntityError(BaseModel):
    type: str
    error_uuid: list[str]
    errors: List[Dict[str, Any]]
