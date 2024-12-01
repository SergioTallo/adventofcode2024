import pytest
from day_1.day_1 import calculate_similarity_score, calculate_distance


def test_calculate_distance():
    assert calculate_distance('test1.txt') == 11

def test_calculate_similarity_score():# add assertion here
    assert calculate_similarity_score('test1.txt') == 31