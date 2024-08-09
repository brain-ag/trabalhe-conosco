from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from typing import Optional


class AreaByState(BaseModel):
    estado: Optional[str] = None
    total: Optional[Decimal] = None


class AreaByCulture(BaseModel):
    cultura: Optional[str] = None
    total: Optional[Decimal] = None


class SoilUse(BaseModel):
    total_agricultavel: Optional[Decimal] = None
    total_vegetacao: Optional[Decimal] = None


class AreaByStatePizza(BaseModel):
    estado: Optional[str] = None
    porcentagem: Optional[Decimal] = None


class AreaByCulturePizza(BaseModel):
    cultura: Optional[str] = None
    porcentagem: Optional[Decimal] = None


class SoilUsePizza(BaseModel):
    porcentagem_agricultavel: Optional[Decimal] = None
    porcentagem_vegetacao: Optional[Decimal] = None


class DashboardDto(BaseModel):
    total_fazendas: Optional[int] = None
    total_hectares: Optional[Decimal] = None
    grafico_pizza_estado: Optional[list[AreaByStatePizza]] = None
    grafico_pizza_cultura: Optional[list[AreaByCulturePizza]] = None
    grafico_pizza_uso_solo: Optional[SoilUsePizza] = None
