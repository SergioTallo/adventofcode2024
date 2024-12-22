from typing import List
import re

from utils_for_adventofcode.line_manipulation import read_lines
from utils_for_adventofcode.time import measure_time
from utils_for_adventofcode.download import download_input

@measure_time
def main():
    print(f'Day 1:')
    download_input(2024, 3, 'session_cookie.txt')
    first_star = calculate_mul_instructions(input_file='day_3/input_day3.txt')
    print(f"First star: {first_star}")
    second_star = calculate_mul_instructions(input_file='day_3/input_day3.txt', second_star=True)
    print(f"Second star: {second_star}")
    print(f"Second star: {check()}")

def check():
    total1 = total2 = 0
    enabled = True
    data = open('day_3/input_day3.txt').read()

    for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
        if do or dont:
            enabled = bool(do)
        else:
            x = int(a) * int(b)
            total1 += x
            total2 += x * enabled
    return total2

@measure_time
def calculate_mul_instructions(input_file: str, second_star: bool = False) -> int:
    lines = read_lines(input_file)
    total_instructions = 0
    for line in lines:
        if second_star:
            line = delete_unused_instructions(line)
        total_instructions += multiply(multiplications=find_correct_multiplications(input_string=line))
    return total_instructions

def find_correct_multiplications(input_string: str) -> List[tuple[str, str]]:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input_string)
    return matches

def multiply(multiplications: list[tuple[str, str]]) -> int:
    total_multiplication = 1
    for multiplication in multiplications:
        total_multiplication += int(multiplication[0]) * int(multiplication[1])
    return total_multiplication - 1


def delete_unused_instructions(input_string: str) -> str:
    pattern = r"don't\(\).*?do\(\)"
    output_string = re.sub(pattern, "", input_string)
    return re.sub(r"don't\(\).*", "", output_string)


if __name__ == '__main__':
    main()
