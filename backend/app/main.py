from fastapi import FastAPI

app = FastAPI(
    title="Seleção FESF-SUS – 1 F.C",
    description="API desenvolvida para o Processo Seletivo FESF-SUS – 1 F.C",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {
        "message": "API da Seleção FESF-SUS funcionando com FastAPI"
    }