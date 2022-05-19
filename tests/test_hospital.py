import pytest

from src.doctor import Doctor
from src.hospital import Hospital
from src.patient import Patient


@pytest.fixture()
def hospital():
    return Hospital("advance clinique")


class TestHospital:
    def test_hospital_instantiation(self, hospital):
        assert isinstance(hospital, Hospital)

    def test_hosiptal_with_bad_name_non_alnum(self):
        with pytest.raises(TypeError):
            Hospital(1520)

    def test_nom_hospital(self, hospital):
        assert hospital.nom == "Advance Clinique"

    def test_doctors_list(self, hospital):
        assert isinstance(hospital.doctors, Doctor)

    def test_patients_list(self):
        assert isinstance(hospital.patients, Patient)

    def test_hospitals_patientslist_is_patienttype(self, hospital):
        assert all([patient for patient in hospital.patients if isinstance(patient, Patient)])

    def test_hospitals_doctorslist_is_doctortype(self, hospital):
        assert all([doctor for doctor in hospital.doctors if isinstance(doctor, Doctor)])
