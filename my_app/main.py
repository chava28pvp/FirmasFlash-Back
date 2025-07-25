from fastapi import FastAPI
from my_app.db.database import engine, Base
from my_app.controller import firmas_controller, archive_controller, users_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Users & Roles API",
    description="Manejo de usuarios y roles conectados a SQL Server",
    version="1.0.0",
    debug=True
)


app.include_router(firmas_controller.router)
app.include_router(archive_controller.router)
app.include_router(users_controller.router)



