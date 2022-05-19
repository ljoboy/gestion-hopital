import datetime
import random

import pytest

from src.patient import Patient


@pytest.fixture()
def patient():
    genre = ["m", "f"]
    return Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", random.choice(genre))


class TestPatient:
    def test_case01(self, patient):
        """Test with good params"""
        assert isinstance(patient, Patient)

    def test_case01_01(self):
        with pytest.raises(TypeError):
            patient = Patient(1, "prenom", "postnom", "+1234567890", "1994-10-17", "m")

    def test_case01_02(self):
        with pytest.raises(TypeError):
            patient = Patient("nom", 2.3, "postnom", "+1234567890", "1994-10-17", "m")

    def test_case01_03(self):
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", True, "+1234567890", "1994-10-17", "m")

    def test_case01_04(self):
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", "postnom", ["+1234567890"], "1994-10-17", "m")

    def test_case01_04(self):
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", "postnom", "jonathan", "1994-10-17", "m")

    def test_case01_05(self):
        with pytest.raises(ValueError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "just une date", "m")

    def test_case01_06(self):
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", object(), "m")

    def test_case01_07(self, patient):
        assert isinstance(patient.nom, str) and isinstance(patient.prenom, str) and isinstance(patient.postnom, str) \
               and isinstance(patient.dob, datetime.date) and isinstance(patient.genre, str)

    def test_case01_08(self):
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", 9)

    def test_case01_09(self):
        with pytest.raises(ValueError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", "masculin")

    def test_case01_10(self):
        with pytest.raises(ValueError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", "g")

    @pytest.mark.skip()
    def test_case22_01(self, patient):
        assert isinstance(patient.age, int)

    @pytest.mark.skip()
    def test_case22_02(self, patient):
        assert isinstance(patient.nom_complet, str) and patient.nom_complet == (
                    patient.nom.upper() + " " + patient.postnom.upper() + " " + patient.prenom.capitalize())


if __name__ == '__main__':
    pytest.testmod()
