from pydantic import BaseModel, Field
from typing import List, Optional


class ApoliceDO(BaseModel):
    seguradora: Optional[str] = None
    segurado_tomador: Optional[str] = None
    numero_apolice: Optional[str] = None

    inicio_vigencia: Optional[str] = None
    fim_vigencia: Optional[str] = None

    limite_maximo_indenizacao: Optional[str] = None
    franquia: Optional[str] = None

    coberturas: List[str] = Field(default_factory=list)
    exclusoes: List[str] = Field(default_factory=list)

    retroatividade: Optional[str] = None
    ambito_territorial: Optional[str] = None