import re
import pytest
from src.doctor import Doctor


@pytest.fixture()
def doctor():
    return Doctor("nom", "prenom", "postnom", "+1234567890")


class TestDoctor:

    def test_case01(self, doctor):
        """ Test if we can instantiate doctor and get a Doctor type with no error """
        assert isinstance(doctor, Doctor)

    def test_case02_01(self):
        """ Test if it's raise an Exception (TypeError) when instantiate without params """
        with pytest.raises(TypeError):
            d1 = Doctor()

    def test_case02_02(self):
        """ Test if it's raise an Exception (TypeError) when instantiate with one params """
        with pytest.raises(TypeError):
            d1 = Doctor("nom")

    def test_case02_03(self):
        """ Test if it's raise an Exception (TypeError) when instantiate with two params """
        with pytest.raises(TypeError):
            d1 = Doctor("nom", "prenom")

    def test_case02_04(self):
        """ Test if it's raise an Exception (TypeError) when instantiate with three params """
        with pytest.raises(TypeError):
            d1 = Doctor("nom", "prenom", "postnom")

    def test_case03_01(self):
        """ Test if it's raise an Exception with bad params """
        with pytest.raises(TypeError):
            d1 = Doctor(2.2, "prenom", "postnom", "phone")

    def test_case03_02(self):
        """ Test if it's raise an Exception with bad params """
        with pytest.raises(TypeError):
            d1 = Doctor("nom", 3, "postnom", "phone")

    def test_case03_03(self):
        """ Test if it's raise an Exception with bad params """
        with pytest.raises(TypeError):
            d1 = Doctor("nom", "prenom", False, "phone")

    def test_case03_04(self):
        """ Test if it's raise an Exception with bad params """
        with pytest.raises(TypeError):
            d1 = Doctor("nom", "prenom", "postnom", ['telephone'])

    def test_case03_05(self):
        """ Test if it's raise an Exception with phone number """
        with pytest.raises(TypeError):
            d1 = Doctor("nom", "prenom", "postnom", "+1234")

    def test_case04(self, doctor):
        """ Test if we can get specialization and it's an empty array """
        assert doctor.specialization == []

    def test_case05_01(self, doctor):
        """ Test if we can assign specialization with list and str to doctor """
        specs = ['Gynecology', "pediatry".capitalize()]
        spec = 'Traumatologie'
        doctor.specialization = specs
        doctor.specialization = spec
        specs = [specs[0].lower(), specs[1].lower(), spec.lower()]
        assert doctor.specialization == specs

    def test_case05_02(self, doctor):
        """ Test if int with raise TypeError """
        with pytest.raises(TypeError):
            doctor.specialization = 55

    def test_case05_03(self, doctor):
        """ Test if an array with a bad type will raise TypeError """
        with pytest.raises(TypeError):
            doctor.specialization = ["Radiology", True]

    def test_case05_04(self, doctor):
        """ Ensure that all upper words will be returned as lower """
        spec = "DENTISTE"
        doctor.specialization = spec
        assert [spec.lower()] == doctor.specialization

    def test_case06_01(self, doctor):
        """ Test if matricule it's generated and if it's a string and match a certain regex """
        matricule = doctor.matricule
        m = re.fullmatch(r"\d{2}[A-Z\d]{2}\d{3}", matricule)
        assert isinstance(matricule, str) and isinstance(m, re.Match)

    def test_case06_02(self):
        """ Test if the last part of matricule it's incremented """
        d1 = Doctor("Wabu", "Roland", "Tubongye", "+1234567890")
        d2 = Doctor("Bushiri", "Kevin", "Abrantes", "+1234567880")
        m1 = d1.matricule
        m2 = d2.matricule

        assert int(m1[-3:]) + 1 == int(m2[-3:])

    def test_case06_03(self):
        """ Try to see if matricule generator works perfectly """
        d1 = Doctor("Wabu", "Roland", "Tubongye", "+1234567890")
        assert (d1.matricule == '22WT001')


if __name__ == '__main__':
    pytest.testmod()
