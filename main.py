from fastapi import FastAPI
from controllersProyect import routers
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# NOTE - 
#  @templates - Directorio de las plantillas
#  @statics - Directorio de css
#  @js - Directorio de Javascript

templates = Jinja2Templates(directory="templates/")

engi = FastAPI()
for router in routers:
    engi.include_router(router)

engi.title = "Engi"

# Para cambiar la version de la aplicacion
engi.version = "0.0.1"
engi.mount("/static", StaticFiles(directory="assets"), name="static")

@engi.get("/", tags=["home"])
def home(request: Request):
    return templates.TemplateResponse("/index.html", {"request": request})
