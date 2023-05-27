from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/api/")
async def read_root():
    return {"version": "0.0.1"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
