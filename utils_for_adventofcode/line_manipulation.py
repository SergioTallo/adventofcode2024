from typing import List

def read_lines(input_file: str) -> List[str]:
    """
    Read each line of text file and return a list of strings containing the lines of input file
    :param input_file: filepath to read in string format
    :return: list of strings containing the lines of input file
    """
    # Read each line of text file
    with open(input_file, 'r') as file:
        data = file.read().splitlines()
    return data

def transform_to_list_of_int(data: List[str]) -> List[List[int]]:
    """
    Transform a list of strings into a list of lists of int
    :param data:
    :return:
    """
    return [[int(x) for x in line.split()] for line in data]

def transform_to_list_of_char(data: List[str]) -> List[List[str]]:
    """
    Transform a list of strings into a list of lists of characters
    :param data:
    :return:
    """
    return [list(line) for line in data]