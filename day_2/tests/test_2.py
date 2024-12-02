from day_2.day_2 import sum_of_reports, is_safe, is_safe_removing_one_level

def test_is_safe():
    assert is_safe([7, 6, 4, 2, 1]) is True
    assert is_safe([1, 2, 7, 8, 9]) is False
    assert is_safe([9, 7, 6, 2, 1]) is False
    assert is_safe([1, 3, 2, 4, 5]) is False
    assert is_safe([8, 6, 4, 4, 1]) is False
    assert is_safe([1, 3, 6, 7, 9]) is True

    assert is_safe_removing_one_level(report=[7, 6, 4, 2, 1]) is True
    assert is_safe_removing_one_level(report=[1, 2, 7, 8, 9]) is False
    assert is_safe_removing_one_level(report=[9, 7, 6, 2, 1]) is False
    assert is_safe_removing_one_level(report=[1, 3, 2, 4, 5]) is True
    assert is_safe_removing_one_level(report=[8, 6, 4, 4, 1]) is True
    assert is_safe_removing_one_level(report=[1, 3, 6, 7, 9]) is True

def test_sum_of_reports():
    assert sum_of_reports('test1.txt') == 2
    assert sum_of_reports('test1.txt', safe_dumper=True) == 4
