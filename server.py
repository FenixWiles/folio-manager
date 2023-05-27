from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
async def home(request: Request):
    context = {"request": request, "message": "Hello, FastAPI with Jinja2!"}
    return templates.TemplateResponse("index.html", context)


@app.get("/about")
async def contact(request: Request):
    context = {"request": request, "message": "Hello, FastAPI with Jinja2!"}
    return templates.TemplateResponse("about.html", context)


@app.get("/contact")
async def contact(request: Request):
    context = {"request": request, "message": "Hello, FastAPI with Jinja2!"}
    return templates.TemplateResponse("contact.html", context)


@app.get("/faq")
async def faq(request: Request):
    context = {"request": request, "message": "Hello, FastAPI with Jinja2!"}
    return templates.TemplateResponse("faq.html", context)


@app.get("/features")
async def faq(request: Request):
    context = {"request": request, "message": "Hello, FastAPI with Jinja2!"}
    return templates.TemplateResponse("features.html", context)


@app.get("/api/")
async def read_root():
    return {"version": "0.0.1"}
