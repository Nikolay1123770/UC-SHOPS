from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "UC SHOP API запущен."}

@app.get("/privacy-policy")
def privacy_policy():
    return FileResponse("html/privacy-policy.html", media_type="text/html")

@app.get("/terms-of-service")
def terms_of_service():
    return FileResponse("html/terms-of-service.html", media_type="text/html")
