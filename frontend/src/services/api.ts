const API_BASE_URL = "http://127.0.0.1:8000";

export type Patient = {
  id: number;
  name: string;
  cpf: string;
  birth_date: string;
  city: string;
  phone?: string | null;
  health_card_number?: string | null;
  created_at: string;
};

export type Appointment = {
  id: number;
  patient_id: number;
  service_type: string;
  professional_name: string;
  status: "pending" | "in_progress" | "completed" | "cancelled";
  notes?: string | null;
  created_at: string;
};

export type DashboardSummary = {
  total_patients: number;
  total_appointments: number;
  pending_appointments: number;
  in_progress_appointments: number;
  completed_appointments: number;
};

export async function getDashboardSummary(): Promise<DashboardSummary> {
  const response = await fetch(`${API_BASE_URL}/dashboard/`);

  if (!response.ok) {
    throw new Error("Erro ao buscar resumo do dashboard");
  }

  return response.json();
}

export async function getPatients(): Promise<Patient[]> {
  const response = await fetch(`${API_BASE_URL}/patients/`);

  if (!response.ok) {
    throw new Error("Erro ao buscar pacientes");
  }

  return response.json();
}

export async function getAppointments(): Promise<Appointment[]> {
  const response = await fetch(`${API_BASE_URL}/appointments/`);

  if (!response.ok) {
    throw new Error("Erro ao buscar atendimentos");
  }

  return response.json();
}