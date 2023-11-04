from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from controllersProyect import routers
from fastapi import requests


engi = FastAPI()
for router in routers: 
    engi.include_router(router)

engi.title = "Proyecto productividad"

#Para cambiar la version de la aplicacion
# engi.version = "0.0.1"

@engi.get("/", tags=['cast'])
def home():
    return HTMLResponse('<h1>Hola mundo</h1>')

