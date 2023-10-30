from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory='templates/')

productividad = APIRouter()
class Productividad:
    @productividad.get('/productividad/', tags=['Productividad'])
    async def view(request: Request):
        return templates.TemplateResponse('index.html',{"request": request})
    
