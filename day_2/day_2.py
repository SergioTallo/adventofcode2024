from typing import List

from utils_for_adventofcode.line_manipulation import transform_to_list_of_int, read_lines
from utils_for_adventofcode.time import measure_time
from utils_for_adventofcode.download import download_input

@measure_time
def main():
    print(f'Day 2:')
    download_input(2024, 2, 'session_cookie.txt')
    first_star = sum_of_reports('day_2/input_day2.txt')
    print(f"First star: {first_star}")
    second_star = sum_of_reports('day_2/input_day2.txt', safe_dumper=True)
    print(f"Second star: {second_star}")

def sum_of_reports(input_file: str, safe_dumper: bool = False) -> int:
    reports_transformed = transform_to_list_of_int(data=read_lines(input_file=input_file))
    sum_of_reports = 0
    for report in reports_transformed:
        if safe_dumper:
            sum_of_reports += is_safe_removing_one_level(report)
        else:
            sum_of_reports += is_safe(report)
    return sum_of_reports

def is_safe(report: List[int]) -> bool:
    for count in range(0, len(report) - 1):
        if abs(report[count] - report[count + 1]) > 3:
            return False
    if not (all(report[i] > report[i + 1] for i in range(len(report) - 1)) or all(
            report[i] < report[i + 1] for i in range(len(report) - 1))):
        return False
    return True

def is_safe_removing_one_level(report: List[int]) -> bool:
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False


if __name__ == '__main__':
    main()