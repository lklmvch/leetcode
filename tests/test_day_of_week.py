import pytest
from day_of_week import dayOfTheWeek


@pytest.mark.parametrize('day, month, year, expected_result', [(31, 8, 2019, "Saturday"),
                                                               (18, 7, 1999, "Sunday"),
                                                               (15, 8, 1993, "Sunday")])
def test_dayOfTheWeek(day, month, year, expected_result):
    assert dayOfTheWeek(day, month, year) == expected_result
