from collections import Counter
from utils_for_adventofcode.line_manipulation import read_lines, transform_to_list_of_int
from utils_for_adventofcode.time import measure_time
from utils_for_adventofcode.download import download_input

@measure_time
def main():
    print(f'Day 1:')
    download_input(2024, 1, 'session_cookie.txt')
    print(f"First star: {calculate_distance('day_1/input_day1.txt')}")
    print(f"Second star: {calculate_similarity_score('day_1/input_day1.txt')}")

def _transform_lists(input_file: str):
    lines = transform_to_list_of_int(read_lines(input_file=input_file))
    first_column = sorted([int(line[0]) for line in lines])
    second_column = sorted([int(line[1]) for line in lines])
    return first_column, second_column

@measure_time
def calculate_distance(input_file: str):
    first_column, second_column = _transform_lists(input_file=input_file)
    total_distance = 0
    for count, line in enumerate(first_column):
        total_distance += abs(first_column[count] - second_column[count])
    return total_distance

@measure_time
def calculate_similarity_score(input_file: str):
    first_column, second_column = _transform_lists(input_file=input_file)
    counted_lines = Counter(second_column)
    sim_score = 0
    for number in first_column:
        if number in counted_lines:
            sim_score += counted_lines[number] * number
    return sim_score


if __name__ == '__main__':
    main()
