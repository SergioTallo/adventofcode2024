from utils_for_adventofcode.time import measure_time
from utils_for_adventofcode.download import download_input
from aocd.models import Puzzle

@measure_time
def main():
    print(f'Day 2:')
    #download_input(2024, 2, 'session_cookie.txt')
    puzzle = Puzzle(year=2024, day=1)
    print(puzzle)
    print(f"First star: ")
    print(f"Second star: ")


if __name__ == '__main__':
    main()