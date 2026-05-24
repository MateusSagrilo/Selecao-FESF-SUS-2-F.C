from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class PatientBase(BaseModel):
    name: str
    cpf: str
    birth_date: date
    city: str
    phone: Optional[str] = None
    health_card_number: Optional[str] = None


class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    cpf: Optional[str] = None
    birth_date: Optional[date] = None
    city: Optional[str] = None
    phone: Optional[str] = None
    health_card_number: Optional[str] = None

class PatientResponse(PatientBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class AppointmentBase(BaseModel):
    patient_id: int
    service_type: str
    professional_name: str
    status: str = "pending"
    notes: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True