from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world from FastAPI"}


@app.get("/health")
def health():
    return {"status": "ok"}