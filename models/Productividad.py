from pydantic import BaseModel, Field
from typing import Optional


class Vogel(BaseModel):
    qo: float  # bpd gasto de aceite
    pr: float  # Presion media del yacimiento psia
    pwf: float  # Presion de fondo fluyente psia
    pb: float  # Presion de Poro psia
    r: int  # Es el numero de iteraciones para la grafica


class VogelArray(BaseModel):
    qo: float  # bpd gasto de aceite
    pr: float  # Presion media del yacimiento psia
    pwf: float  # Presion de fondo fluyente psia
    pb: float  # Presion de Poro psia
    r: list[float] = Field(default_factory=lambda: [i for i in range(pr, 0, -50)])

    def __init__(self, pr: float, **data):
        super().__init__(**data)
        self.pr = pr
        self.r = [i for i in range(self.pr, 0, -50)]
