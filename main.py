from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes import cita

app = FastAPI()
app.title = "BarberBOT" 
app.version = "1.0.0"
app.include_router(cita.router)

@app.get("/", tags=['Inicio'])
def message():
    return HTMLResponse(content="<h1> Bienvenido a BarberBOT</h1>")