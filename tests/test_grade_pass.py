import pytest
from src.grade_pass import has_passed

@pytest.mark.parametrize(
    "score, expected_pass",
    [
        (90, True),
        (75, True),
        (50, True),
        (49, False),
        (0, False),
    ],
)   

def test_grade_pass(score, expected_pass):
    result = has_passed(score)
    assert result == expected_pass

@pytest.mark.parametrize(
    "score, expected_error",
    [
        (-10, ValueError),  # Invalid score
        (110, ValueError),  # Invalid score
        ("A", TypeError), #Invalid type
        ("", TypeError )  # Invalid type
    ],
)

def test_grade_pass_invalid_input(score, expected_error):
    with pytest.raises(expected_error):
        has_passed(score)  # Invalid input