import pytest
from src.grade_average import calculate_average

@pytest.mark.parametrize(
    "mark_one, mark_two, expected_average",
    [
        (90, 80, 85.0),
        (75, 85, 80.0),
        (60, 70, 65.0),
        (50, 50, 50.0),
        (0, 100, 50.0),
    ] 
)

def test_grade_average(mark_one, mark_two, expected_average):
    result = calculate_average(mark_one, mark_two)
    assert result == expected_average

@pytest.mark.parametrize(
    "mark_one, mark_two, expected_error",
    [
        (-10, 80, ValueError),  # Invalid mark_one
        (80, -10, ValueError),  # Invalid mark_two
        (110, 80, ValueError),  # Invalid mark_one
        (80, 110, ValueError),  # Invalid mark_two
        ("A", 80, TypeError),  # Invalid type for mark_one
        (80, "B", TypeError),  # Invalid type for mark_two
    ],
)

def test_grade_average_invalid_input(mark_one, mark_two, expected_error):
    with pytest.raises(expected_error):
        calculate_average(mark_one, mark_two)  # Invalid input
