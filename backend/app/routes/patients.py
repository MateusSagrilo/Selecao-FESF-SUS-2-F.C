from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.database import get_db
from app.models import Patient
from app.schemas import PatientCreate, PatientResponse


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/", response_model=PatientResponse)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    db_patient = Patient(
        name=patient.name,
        cpf=patient.cpf,
        birth_date=patient.birth_date,
        city=patient.city,
        phone=patient.phone,
        health_card_number=patient.health_card_number
    )

    db.add(db_patient)

    db.commit()

    db.refresh(db_patient)

    return db_patient