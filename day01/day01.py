import re
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


number_names = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


regex = re.compile('(?=(' + '|'.join([r'\d', *number_names]) + '))')


def get_first_and_last_digits(line: str) -> tuple[int, int]:
    digits = [int(number_names.get(d, d)) for d in regex.findall(line)]
    return digits[0], digits[-1]


@pytest.mark.parametrize(
    ['line', 'expected'],
    [
        ('a1b2c3d4e5f', 15),
        ('treb7uchet', 77),
        ('7pqrstsixteen', 76),
        ('xtwone3four', 24),
        ('two1nine', 29),
        ('eightwothree', 83),
        ('abcone2threexyz', 13),
        ('4nineeightseven2', 42),
        ('zoneight234', 14),
        ('oneoneightabcdfe', 18),
    ]
)
def test_extract_number_from_line_2(line, expected):
    assert expected == extract_number_from_line(line)


test_input_2 = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen\
"""


def test_sum_numbers_on_lines_of_text_2():
    assert 281 == sum_numbers_on_lines_of_text(test_input_2)


if __name__ == '__main__':
    p2 = sum_numbers_on_lines_of_text(puzzle_input)
    print(f'Part 2: {p2}')