from logging import exception

import requests
import os

def download_input(year: int, day: int, cookie_file_path: str):
    """
    Download input file from Advent of Code website and save it in the current directory
    :param year: year of the challenge
    :param day: day of the challenge
    :param cookie_file_path: filepath to read in string format
    :return: None
    """
    if not os.path.exists(f'day_{day}/input_day{day}.txt'):
        session_cookie = ''
        if os.path.exists(cookie_file_path):
            with open(cookie_file_path, 'r') as file:
                session_cookie = file.read().strip()
        else:
            print("Session cookie file not found.")

        cookies = {'session': session_cookie}

        url = f'https://adventofcode.com/{year}/day/{day}/input'
        response = requests.get(url, cookies=cookies)

        if response.status_code == 200:
            try:
                with open(f'day_{day}/input_day{day}.txt', 'w') as file:
                    file.write(response.text)
            except Exception as ex:
                print(f'Exception: {ex}')
        else:
            print(f"Failed to download input for day {day}. Status code: {response.status_code}")
    else:
        print(f"Input file 'day_{day}/input_day{day}.txt already exists.")