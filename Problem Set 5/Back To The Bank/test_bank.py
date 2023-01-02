from bank import value

def main():
    test_0()
    test_20()
    test_100()

def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_20():
    assert value("hey, what's up?") == 20
    assert value("Hey, what's happening?") == 20

def test_100():
    assert value("what's up?") == 100
    assert value("What's happening?") == 100

if __name__ == "__main__":
    main()