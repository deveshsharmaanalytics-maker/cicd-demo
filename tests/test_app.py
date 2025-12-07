from app import add

def test_add():
    assert add(5, 7) == 12
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
