from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Patient
from app.schemas import PatientCreate, PatientResponse


router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post(
    "/",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED
)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):
    existing_patient = db.query(Patient).filter(
        Patient.cpf == patient.cpf
    ).first()

    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Já existe um paciente cadastrado com este CPF."
        )

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


@router.get(
    "/",
    response_model=List[PatientResponse]
)
def list_patients(
    db: Session = Depends(get_db)
):
    patients = db.query(Patient).order_by(Patient.created_at.desc()).all()

    return patients


@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def get_patient_by_id(
    patient_id: int,
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(
        Patient.id == patient_id
    ).first()

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paciente não encontrado."
        )

    return patient