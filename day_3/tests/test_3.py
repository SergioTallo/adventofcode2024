from day_3.day_3 import find_correct_multiplications, multiply, calculate_mul_instructions, delete_unused_instructions

def test_find_correct_multiplications():
    assert find_correct_multiplications('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))') == [
        ('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]

def test_multiply():
    assert multiply([('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]) == 161

def test_calculate_mul_instructions():
    assert calculate_mul_instructions('test3.txt') == 161

def test_delete_unused_instructions():
    assert (delete_unused_instructions("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") ==
            "xmul(2,4)&mul[3,7]!^?mul(8,5))")

    assert (delete_unused_instructions("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)un?mul(8,5))") ==
            "xmul(2,4)&mul[3,7]!^")