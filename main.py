from fastapi import FastAPI


app = FastAPI(title="User Management API")


@app.get("/")
async def root():
    return {"Hello world!"}
