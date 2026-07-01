from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI -> Uvicorn
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world from FastAPI"}


@app.get("/health")
def health():
    return {"status": "ok"}

class LoginRequest(BaseModel):
    phone: str
    code: str

@app.post("/login")
def login(data: LoginRequest):
    return {"status": "ok", "phone": data.phone}