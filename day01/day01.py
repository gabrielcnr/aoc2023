from pathlib import Path

import pytest


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


def sum_numbers_on_lines_of_text(text: str) -> int:
    lines = text.splitlines()
    return sum(extract_number_from_line(line) for line in lines)


test_input = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet\
"""


def test_sum_numbers_on_lines_of_text():
    assert 142 == sum_numbers_on_lines_of_text(test_input)


if __name__ == '__main__':
    puzzle_input = open(Path(__file__).parent / 'input.txt').read()

    p1 = sum_numbers_on_lines_of_text(puzzle_input)
    print(f'Part 1: {p1}')
   