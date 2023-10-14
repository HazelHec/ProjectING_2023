from fastapi import FastAPI

app = FastAPI()


@app.route('/')
def index():
    return "Hola mundo"