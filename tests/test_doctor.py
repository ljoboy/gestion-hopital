import pytest
from src.doctor import Doctor


class TestDoctor:

    def test_case01(self):
        """ Test if it's record all Doctor infos """
        d1 = Doctor("nom", "prenom", "postnom", "phone")
        assert isinstance(d1, Doctor)

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
            d1 = Doctor("nom", "prenom", "postnom", ['telephone'])

    def test_case03_04(self):
        """ Test if it's raise an Exception with bad params """
        with pytest.raises(TypeError):
            d1 = Doctor("nom", "prenom", "postnom", ['telephone'])


if __name__ == '__main__':
    pytest.testmod()
