from twttr import shorten

def main():
    test_upper()
    test_lower()
    test_other()

def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("BEAUTIFUL") == "BTFL"

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("beautiful") == "btfl"

def test_other():
    assert shorten("cs50") == "cs50"
    assert shorten("ObViOuSlY") == "bVSlY"
    assert shorten("12345") == "12345"
    assert shorten("twitter.py") == "twttr.py"

if __name__ == "__main__":
    main()