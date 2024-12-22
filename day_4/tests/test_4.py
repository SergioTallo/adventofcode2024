from day_4.day_4 import count_xmas, count_x_mas
from utils_for_adventofcode.line_manipulation import read_lines

def test_count_xmas():
    assert count_xmas(grid=read_lines('test4.txt')) == 18

def test_count_x_mas():
    assert count_x_mas(grid=read_lines('test4.txt')) == 9