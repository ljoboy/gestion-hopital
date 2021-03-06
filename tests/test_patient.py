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
        """Test to instantiate with good params"""
        assert isinstance(patient, Patient)

    def test_case01_01(self):
        """Test to instantiate with bad params"""
        with pytest.raises(AttributeError):
            patient = Patient(1, "prenom", "postnom", "+1234567890", "1994-10-17", "m")

    def test_case01_02(self):
        """Test to instantiate with bad params"""
        with pytest.raises(AttributeError):
            patient = Patient("nom", 2.3, "postnom", "+1234567890", "1994-10-17", "m")

    def test_case01_03(self):
        """Test to instantiate with bad params"""
        with pytest.raises(AttributeError):
            patient = Patient("nom", "prenom", True, "+1234567890", "1994-10-17", "m")

    def test_case01_04(self):
        """Test to instantiate with bad params"""
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", "postnom", ["+1234567890"], "1994-10-17", "m")

    def test_case01_11(self):
        """Test to instantiate with bad params"""
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", "postnom", "jonathan", "1994-10-17", "m")

    def test_case01_05(self):
        """Test to instantiate with bad params"""
        with pytest.raises(ValueError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "just une date", "m")

    def test_case01_06(self):
        """Test to instantiate with bad params"""
        with pytest.raises(TypeError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", object(), "m")

    def test_case01_07(self, patient):
        """Test to instantiate with bad params"""
        assert isinstance(patient.nom, str) and isinstance(patient.prenom, str) and isinstance(patient.postnom, str) \
               and isinstance(patient.dob, datetime.date) and isinstance(patient.genre, str)

    def test_case01_08(self):
        """Test to instantiate with bad params"""
        with pytest.raises(AttributeError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", 9)

    def test_case01_09(self):
        """Test to instantiate with bad params"""
        with pytest.raises(ValueError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", "masculin")

    def test_case01_10(self):
        """Test to instantiate with bad params"""
        with pytest.raises(ValueError):
            patient = Patient("nom", "prenom", "postnom", "+1234567890", "1994-10-17", "g")

    def test_case22_01(self, patient):
        """Test if age property it's working"""
        assert isinstance(patient.age, int) and patient.age == datetime.date.today().year - 1994

    def test_case22_02(self, patient):
        """Test if nom_complet property it's working"""
        assert isinstance(patient.nom_complet, str) and patient.nom_complet == (
                patient.nom.upper() + " " + patient.postnom.upper() + " " + patient.prenom.capitalize())

    def test_a_numdossier(self, patient):
        """Test if num_dossier it's generated"""
        assert patient.num_dossier.startswith("NM")

    def test_mesures_patient(self, patient):
        patient.mesures(72, 182)
        assert patient.taille == 182 and patient.poids == 72

    def test_mesures_taille_not_numeric(self, patient):
        with pytest.raises(TypeError):
            patient.mesures("98.08", 9)

    def test_mesures_poids_not_integer(self, patient):
        with pytest.raises(TypeError):
            patient.mesures(98, 9.8)

    def test_phone_property(self, patient):
        assert patient.phone == "+1234567890"

    def test_patient_str(self, patient):
        assert str(patient) == "Prenom NOM POSTNOM"

    def test_add_patient_plaintes(self, patient):
        p = "Maux de t??te"
        patient.plaintes = p
        assert p in patient.plaintes

    def test_add_plaintes_with_error(self, patient):
        with pytest.raises(TypeError):
            patient.plaintes = ["Fi??vre", "Toux"]


if __name__ == '__main__':
    pytest.testmod()
