from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡Hola! Bienvenido a mi primera API con FastAPI"}

@app.get("/info")
def get_info():
    return {
        "api_name": "Mi Primera API",
        "version": "1.0",
        "author": "Leonel Rodriguez"
    }

@app.get("/my-profile")
def my_profile():
    return {
        "name": "Leonel Rodriguez",
        "bootcamp": "FastAPI",
        "week": 1,
        "date": "2025",
        "likes_fastapi": True
    }