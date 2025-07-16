from fastapi import FastAPI
from app.db.database import engine, Base


app = FastAPI(title="auth Management API")

# Crear tablas (en desarrollo)
Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"Hello world!"}
