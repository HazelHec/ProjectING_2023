from fastapi import FastAPI, HTTPException
from controllersProyect import routers
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from middleware.errorHandler import ErrorHandler
from fastapi.responses import JSONResponse
from jwt_manager import create_token
from core.configLog import log_config   
import uvicorn


# Crear una instancia de FastAPI
# NOTE - 
#  @templates - Directorio de las plantillas
#  @statics - Directorio de css
#  @js - Directorio de Javascript

templates = Jinja2Templates(directory="templates/")

engi = FastAPI(
    # servers=[
    #     # {
    #     #     "url" : "engi/apiv1",
    #     #     "description" : "local host"
    #     # },
    #     {
    #         "url" : "https://192.168.1.11/engi/apiv1",
    #         "description" : "secure path"
    #     }
    # ],
    debug=True,
    root_path="/engi")

#agregar middleware
engi.add_middleware(ErrorHandler) #errores del servidor 

for router in routers:
    engi.include_router(router)

engi.title = "Engi"

# Para cambiar la version de la aplicacion
engi.version = "0.0.1"
engi.mount("/static", StaticFiles(directory="assets"), name="static")

@engi.get("/", tags=["home"])
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@engi.post("/login", tags=["login"])
def about(nombre: str, email: str):
    a = {'nombre':nombre,'email':email}
    b = create_token(a)
    return {"mensaje": f"Bienvenido {nombre} \ntu token es: {b}"}

# Manejar excepcion
@engi.exception_handler(HTTPException)
async def handle_http_exception(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"mensaje_de_error": exc.detail},
    )


#Initialing proyect when exxcute main method

if __name__ == "__main__":
    uvicorn.run(
        "main:engi",
        host="192.168.1.2",
        port=8443,
        reload=True,
        log_config = log_config,
        use_colors=True
        )