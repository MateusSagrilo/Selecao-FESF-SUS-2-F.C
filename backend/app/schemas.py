from enum import Enum
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

class AppointmentStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class AppointmentBase(BaseModel):
    patient_id: int
    service_type: str
    professional_name: str
    status: AppointmentStatus = AppointmentStatus.pending
    notes: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    pass

class AppointmentUpdate(BaseModel):
    service_type: Optional[str] = None
    professional_name: Optional[str] = None
    status: Optional[AppointmentStatus] = None
    notes: Optional[str] = None

class AppointmentResponse(AppointmentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True