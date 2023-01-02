import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("one/two")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"


if __name__ == "__main__":
    main()