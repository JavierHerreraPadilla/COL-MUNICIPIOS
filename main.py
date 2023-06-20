from fastapi import FastAPI, HTTPException, Request
import json
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# templates = Jinja2Templates(directory="./col_departamentos/templates")
templates = Jinja2Templates(directory="./")



with open("deps.json", "r", encoding="utf-8") as f:
    DEPARTAMENTOS = json.load(f)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/all")
def all_departamentos():
    return list(DEPARTAMENTOS.keys())


@app.get("/{departamento}")
def municipios(departamento: str):
    if not DEPARTAMENTOS.get(departamento.title()):
        return HTTPException(status_code=404, detail="Departamento no encontrado")
    municipios = sorted(DEPARTAMENTOS[departamento.title()]["municipios"])
    return {departamento.title(): municipios}
