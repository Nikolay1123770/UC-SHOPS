from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "UC SHOP API + бот работают"}
