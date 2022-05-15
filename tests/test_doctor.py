import pytest
from src.doctor import Doctor


class TestDoctor:

    def test_case01(self):
        """ Test if it's record all Doctor infos """
        self.doctor = Doctor()
        assert isinstance(self.doctor, Doctor)


if __name__ == '__main__':
    pytest.testmod()
