from max_balloons import maxNumberOfBalloons
import pytest



@pytest.mark.parametrize('text, expected_result', [("nlaebolko", 1), ("loonbalxballpoon", 2), ("leetcode", 0)])
def test_maxNumberOfBalloons(text, expected_result):
    assert maxNumberOfBalloons(text) == expected_result
