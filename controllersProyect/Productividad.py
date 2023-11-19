from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates
import json
import pprint

# Importar metodos numericos
from .productividad.Vogel import Vogel
from .productividad.BackPressure import BackPressure
from .productividad.Standing import Standing
from .productividad.Eickmeier import Eickmeier

# Importar modelos
from models import *

templates = Jinja2Templates(directory="templates/Productividad")

productividad = APIRouter()

# NOTE - El metodo quedara para realizarce en futuro
# @productividad.get("/productividad/", tags=["Productividad"])
# async def view(request: Request):
#     return templates.TemplateResponse("/Vogel_generalizado.html", {"request": request})


# NOTE - Voguel Methods
@productividad.get("/productividad/vogel", tags=["Productividad"])
async def indexVogel(request: Request):
    return templates.TemplateResponse("/Vogel_generalizado.html", {"request": request})


@productividad.post("/productividad/vogel", tags=["Productividad"])
async def vogel(data: VogelModel):
    metodo = Vogel()
    if data.pwf >= data.pb:
        caseA = metodo.VogelCaseA(data.qo, data.pr, data.pwf, data.pb, data.r)
        return json.dumps(caseA)
    else:
        caseB = metodo.VogelCaseB(data.qo, data.pr, data.pwf, data.pb, data.r)
        return json.dumps(caseB)


# NOTE - BackPressure Methods
@productividad.get("/productividad/back-pressure", tags=["Productividad"])
async def indexBackPressure(request: Request):
    return templates.TemplateResponse("/back-pressure.html", {"request": request})


@productividad.post("/productividad/back-pressure", tags=["Productividad"])
async def backPresure(data: BackPressureModel):
    response = BackPressure()
    return response.defaultMethod(data.pr, data.pwf1, data.pwf2, data.qg1, data.qg2, data.r)


# NOTE - Eickmeir Methods
@productividad.get("/productividad/eickmeier", tags=["Productividad"])
async def indexEickmeier(request: Request):
    return templates.TemplateResponse("/Eickmeier.html", {"request": request})


@productividad.post("/productividad/eickmeier", tags=["Productividad"])
async def eickmeier(data: EickmeierModel):
    response = Eickmeier()
    return response.defaultMethod(data.qo,data.prP,data.pwf,data.prF)


# NOTE - Stading Methods
@productividad.get("/productividad/standing", tags=["Productividad"])
async def indexStanding(request: Request):
    return templates.TemplateResponse("/standing.html", {"request": request})


@productividad.post("/productividad/standing", tags=["Productividad"])
async def standing(data: StandingModel):
    response = Standing()
    return response.defaultMethod(data.qoP,data.prP,data.pwf,data.prF,data.kroP,data.kroF,data.vizP,data.vizF,data.BoP,data.BoF ,data.r)
