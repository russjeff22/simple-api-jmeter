# main.py
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/status", response_class=PlainTextResponse)
def read_status():
    return "OK"