import pytest
test_input = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet\
"""

def get_first_and_last_digits(line: str) -> tuple[int, int]:
    digits = [int(c) for c in line if c.isdigit()]
    return digits[0], digits[-1]


def extract_number_from_line(line: str) -> int:
    first, last = get_first_and_last_digits(line)
    return first * 10 + last


@pytest.mark.parametrize(
    ['line', 'expected'],
    [
        ('a1b2c3d4e5f', 15),
        ('treb7uchet', 77),
    ]
)
def test_extract_number_from_line(line, expected):
    assert expected == extract_number_from_line(line)