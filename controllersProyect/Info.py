from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates/")

info = APIRouter()

#NOTE - Metodos de texto plano 

@info.get("/biografia", tags=["Info"])
async def biografia(request: Request):
    return templates.TemplateResponse("/Biografia.html", {"request": request})

@info.get("/agradecimientos", tags=["Info"])
async def agradecimientos(request: Request):
    return templates.TemplateResponse("/agradecimientos.html", {"request": request})