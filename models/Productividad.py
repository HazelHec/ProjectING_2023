from pydantic import BaseModel
from typing import List, Dict

# Field
# from typing import Optional


#!SECTION Modales ordinarios de los metodos
class VogelModel(BaseModel):
    qo: float  # bpd gasto de aceite
    pr: float  # Presion media del yacimiento psia
    pwf: float  # Presion de fondo fluyente psia
    pb: float  # Presion de Burbuja psia
    r: int  # Es el numero de iteraciones para la grafica


class VogelResponseModel(BaseModel):
    J: float # IP
    qb: float # correccion del gasto
    qc: float # Segunda correccion del gasto
    lpwf: List[float] #Lista de valores de pwf
    lqob: Dict[float, float] #Directorio bajo saturado
    lqos: Dict[float, float] #Dircectorio saturado


class BackPressureModel(BaseModel):
    pr: float  # Presion
    pwf1: float  # Presion de fondo fluyente punto 1
    pwf2: float  # Presion de fondo fluyente punto 2
    qg1: float  # Gasto del gas punto 1
    qg2: float  # Gasto del gas punto 2
    r: int  # Debe ser entero este es el numero de iteraciones para la grafica


class BackPressureResponseModel(BaseModel):
    m: float # pendiente
    n: float # inversa de la pendiente 
    c: float # constante
    lpwf: List[float] # lista de valores de pwf
    lqg: List[float] # Lista de valores de qg


class EickmeierModel(BaseModel):
    qo: float  # bpd gasto de aceite
    prP: float  # Presión del yacimiento actual
    pwf: float  # Presion de fondo fluyente psia
    prF: float  # Presión del yacimiento futura


class EickmeierResponseModel(BaseModel):
    qoMaxP: float  # Gasto maximo presente
    qoMaxF: float  # Gasto maximo futuro
    qoF: float  # Gasto Maximo


class StandingModel(BaseModel):
    # Calculos de qo EF
    pwf: float  # Presion de fondo fluyente psia
    pr: float  # Presion media del yacimiento psia
    qo: float  # bpd gasto de aceite
    ef: float  # Presion de Burbuja psia
    n: int  # Es el numero de iteraciones para la grafica


class StandingResponseModel(BaseModel):
    pwfs: float  # presion de fondo fluyente con dano
    qoMaxEf1: float  # gasto maximo a EF = 1
    qoMaxEfD: float  # gasto maximo a EF = del usuario
    lpwf: List[float] #valores de pwf 
    lqoEf: List[float] #valores qo para eficiencia dada
    lqoEf1: List[float] #valores qo para eficiencia = 1
