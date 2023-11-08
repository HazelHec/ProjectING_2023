from pydantic import BaseModel

# Field
# from typing import Optional


#!SECTION Modales ordinarios de los metodos
class VogelModel(BaseModel):
    qo: float  # bpd gasto de aceite
    pr: float  # Presion media del yacimiento psia
    pwf: float  # Presion de fondo fluyente psia
    pb: float  # Presion de Burbuja psia
    r: int  # Es el numero de iteraciones para la grafica


class BackPressureModel(BaseModel):
    pr : float  # Presion
    pwf1 : float  # Presion de fondo fluyente punto 1
    pwf2 : float  # Presion de fondo fluyente punto 2
    qg1 : float  # Gasto del gas punto 1
    qg2 : float  # Gasto del gas punto 2
    r : int  # Debe ser entero este es el numero de iteraciones para la grafica


class EickmeierModel(BaseModel):
    qo : float  # bpd gasto de aceite 
    prP : float  # Presión del yacimiento actual
    pwf : float  # Presion de fondo fluyente psia
    prF : float  # Presión del yacimiento futura

class StandingModel(BaseModel):
    #Calculos de qoF y qomaxF

    qoP : float #El gasto presente
    prP : float #Presion media del yacimiento Presente 
    pwf : float #Presion de fondo fluyente
    prF : float #Presion media del yacimiento Futura

    #NOTE - El primer valor de la lista es el presente y el segundo el futuro
    #Tomar esto en cuenta en sus ejercicios de prueba
    kroP : float # kro 
    kroF : float # kro 
    vizP : float #Vizcosidad presente y futura
    vizF : float #Vizcosidad presente y futura
    BoP : float #Bo presente y futuro
    BoF : float #Bo presente y futuro
    r : int #Es el numero de iteraciones para el grafico



    
# class VogelArray(BaseModel):
#     qo: float  # bpd gasto de aceite
#     pr: float  # Presion media del yacimiento psia
#     pwf: float  # Presion de fondo fluyente psia
#     pb: float  # Presion de Poro psia
#     r: list[float] : Field(default_factory:lambda: [i for i in range(pr, 0, -50)])

#     def __init__(self, pr: float, **data):
#         super().__init__(**data)
#         self.pr : pr
#         self.r : [i for i in range(self.pr, 0, -50)]
