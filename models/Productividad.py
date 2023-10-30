from pydantic import BaseModel, Field
from typing import Optional

class Vogel(BaseModel):
    qo = 0.0 #bpd gasto de aceite
    pr = 0.0 #Presion media del yacimiento psia
    pwf = 0.0 #Presion de fondo fluyente psia
    pb = 0.0 #Presion de Poro psia
    r = 0 #Es el numero de iteraciones para la grafica
    id: Optional[int]
    #Validacion para que el titulo no tenga mas de 15 caracteres
    title : str = Field(default="My movie", min_length=4, max_length=15)
    #le para decir que es menor que el numero de la validacion
    year : int = Field(default=2023, le = 2024)
    director : str
    categorias : strclass