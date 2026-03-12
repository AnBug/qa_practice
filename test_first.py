def test_math_fail():
    expected = 10
    actual = 5 + 5
    assert actual == expected, f"Ошибка! Ожидали {expected}, но получили {actual}"
