from pathlib import Path

bag = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

def validate_game(line: str) -> int:
    game_str, sets_str = line.split(':')
    _, game_number = game_str.split()
    sets = sets_str.split(';')
    for set_ in sets:
        balls = set_.split(',')
        for ball in balls:
            count, colour = ball.split()
            count = int(count)
            if count > bag[colour]:
                return 0
    return int(game_number)


def test_validate_game():
    assert 1 == validate_game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
    assert 2 == validate_game('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue')
    assert 0 == validate_game('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red')
    assert 0 == validate_game('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red')
    assert 5 == validate_game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')


def sum_of_valid_game_ids(puzzle_input: str) -> int:
    return sum(game_id for line in puzzle_input.splitlines() if (game_id := validate_game(line)))


def test_sum_of_valid_game_ids():
    test_input = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green\
"""
    assert 8 == sum_of_valid_game_ids(test_input)


if __name__ == '__main__':
    puzzle_input = open(Path(__file__).parent / 'input.txt').read()

    p1 = sum_of_valid_game_ids(puzzle_input)
    print(f'Part 1: {p1}')
