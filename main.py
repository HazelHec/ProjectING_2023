from fastapi import FastAPI, HTTPException
from controllersProyect import routers
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# NOTE - 
#  @templates - Directorio de las plantillas
#  @statics - Directorio de css
#  @js - Directorio de Javascript

templates = Jinja2Templates(directory="templates/")

engi = FastAPI(debug=True)

for router in routers:
    engi.include_router(router)

engi.title = "Engi"

# Para cambiar la version de la aplicacion
engi.version = "0.0.1"
engi.mount("/static", StaticFiles(directory="assets"), name="static")

@engi.get("/", tags=["home"])
def home(request: Request):
    return templates.TemplateResponse("/index.html", {"request": request})
# Manejar excepcion
@engi.exception_handler(HTTPException)
async def handle_http_exception(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"mensaje_de_error": exc.detail},
    )
