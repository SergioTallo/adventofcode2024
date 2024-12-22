from typing import List

from utils_for_adventofcode.line_manipulation import read_lines
from utils_for_adventofcode.time import measure_time
from utils_for_adventofcode.download import download_input

@measure_time
def main():
    print(f'Day 1:')
    download_input(2024, 4, 'session_cookie.txt')
    first_star = count_xmas(grid=read_lines('day_4/input_day4.txt'))
    print(f"First star: {first_star}")
    second_star = count_x_mas(grid=read_lines('day_4/input_day4.txt'))
    print(f"Second star: {second_star}")

@measure_time
def count_xmas(grid: List[str]) -> int:
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]

    count = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if matches(x, y, direction_x=dx, direction_y=dy, grid=grid, word="XMAS"):
                    count += 1
    return count

def matches(x: int, y: int, direction_x: int, direction_y: int, grid: List[str], word: str) -> bool:
    for i in range(len(word)):
        nx, ny = x + i * direction_x, y + i * direction_y
        if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] != word[i]:
            return False
    return True

@measure_time
def count_x_mas(grid: List[str]) -> int:
    count = 0
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            if grid[x][y] == 'A' and matches_x_mas(x, y, grid=grid):
                count += 1
    return count


def matches_x_mas(x: int, y: int, grid: List[str]) -> bool:
    patterns = [
        [(x - 1, y - 1, 'M'), (x - 1, y + 1, 'S'), (x + 1, y - 1, 'M'), (x + 1, y + 1, 'S')],
        [(x - 1, y - 1, 'M'), (x - 1, y + 1, 'M'), (x + 1, y - 1, 'S'), (x + 1, y + 1, 'S')],
        [(x - 1, y - 1, 'S'), (x - 1, y + 1, 'M'), (x + 1, y - 1, 'S'), (x + 1, y + 1, 'M')],
        [(x - 1, y - 1, 'S'), (x - 1, y + 1, 'S'), (x + 1, y - 1, 'M'), (x + 1, y + 1, 'M')]
    ]

    for pattern in patterns:
        if all(grid[nx][ny] == char for nx, ny, char in pattern):
            return True
    return False

if __name__ == '__main__':
    main()
