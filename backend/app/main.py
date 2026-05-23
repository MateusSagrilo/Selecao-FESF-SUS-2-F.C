from fastapi import FastAPI

from app.database import Base, engine
from app import models

from app.routes.patients import router as patients_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Seleção FESF-SUS API",
    description="API desenvolvida com FastAPI para o processo seletivo FESF-SUS",
    version="1.0.0",
)

app.include_router(patients_router)

@app.get("/")
def read_root():
    return {
        "message": "API da Seleção FESF-SUS funcionando com FastAPI"
    }