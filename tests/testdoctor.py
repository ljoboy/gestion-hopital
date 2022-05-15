import unittest
from src.doctor import Doctor


class TestDoctor(unittest.TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.doctor = False

    def test_case01(self):
        """ Test if it's record all Doctor infos """
        self.doctor = Doctor()
        self.assertIsInstance(self.doctor, Doctor)


if __name__ == '__main__':
    unittest.main()
