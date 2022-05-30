import pytest
from src.day import Day


class TestDay:

    def test_enum_with_bad_params(self):
        with pytest.raises(ValueError):
            Day(9)

    def test_enum_with_bad_params2(self):
        with pytest.raises(ValueError):
            Day("Just a msg")

    def test_enum_okay(self):
        assert Day.LUNDI == 0


if __name__ == '__main__':
    pytest.testmod()
