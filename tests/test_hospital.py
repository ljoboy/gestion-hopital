import pytest

from tests.helpers import *
from src.doctor import Doctor
from src.hospital import Hospital
from src.patient import Patient


@pytest.fixture()
def hospital(patient, doctor):
    h = Hospital("advance clinique")
    for i in range(10):
        h.add_patient(patient)
        h.add_doctor(doctor)
    return h


@pytest.fixture()
def patient():
    genre = ["m", "f"]
    return Patient(random_lastname(), random_firstname(), random_lastname(), random_phone_number(),
                   date_generator(), random.choice(genre))


@pytest.fixture()
def doctor():
    return Doctor(random_lastname(), random_firstname(), random_firstname(), random_phone_number())


class TestHospital:
    """
    Test class for hospital
    """

    def test_hospital_instantiation(self, hospital):
        assert isinstance(hospital, Hospital)

    def test_hosiptal_with_bad_name_non_alnum(self):
        with pytest.raises(TypeError):
            Hospital(1520)

    def test_nom_hospital(self, hospital):
        assert hospital.nom == "Advance Clinique"

    def test_doctors_list(self, hospital):
        assert isinstance(hospital.doctors, list)

    def test_patients_list(self, hospital):
        assert isinstance(hospital.patients, list)

    def test_hospitals_patientslist_is_patienttype(self, hospital):
        assert all(isinstance(patient, Patient) for patient in hospital.patients) or hospital.patients == []

    def test_hospitals_doctorslist_is_doctortype(self, hospital):
        assert all(isinstance(doctor, Doctor) for doctor in hospital.doctors) or hospital.doctors == []

    def test_can_add_patient_with_error(self, hospital):
        with pytest.raises(TypeError):
            hospital.add_patient("qwetyuiop")

    def test_can_add_patient(self, hospital, patient):
        hospital.add_patient(patient)
        assert patient in hospital.patients

    def test_can_add_doctor_with_error(self, hospital):
        with pytest.raises(TypeError):
            hospital.add_doctor("qwetyuiop")

    def test_can_add_doctor(self, hospital, doctor):
        hospital.add_doctor(doctor)
        assert doctor in hospital.doctors

    def test_can_search_patient_by_identity_with_one_params(self, hospital):
        patients = hospital.find_patient("ilunga")
        assert all(isinstance(patient, Patient) for patient in patients)

    def test_can_search_patient_by_identity_with_named_params(self, hospital):
        patients = hospital.find_patient(nom="kasongo", postnom="nyembo", prenom="marc")
        assert all(isinstance(patient, Patient) for patient in patients)

    def test_find_patient_by_num_dossier(self, hospital):
        hospital.add_patient(Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", "m"))
        patient = hospital.find_patient_by_num_dossier("NM")
        assert isinstance(patient, Patient) or patient is None

    # def test_show_all_patients(self, hospital):
