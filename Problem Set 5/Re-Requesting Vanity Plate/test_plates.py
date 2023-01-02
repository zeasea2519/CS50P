from plates import is_valid

def main():
    test_punctuation()
    test_length()
    test_start()
    test_num()
    test_other()

def test_punctuation():
    #no punctuation
    assert is_valid("ER.43.2") == False
    assert is_valid("ER$&0") == False
    assert is_valid("$^£&$") == False
    assert is_valid("ER$50") == False
    assert is_valid("ER432") == True

def test_length():
    #must be 2-6 characters
    assert is_valid("ADND4534") == False
    assert is_valid("ADND5") == True

def test_start():
    #must start with 2 letters
    assert is_valid("4DFH3") == False
    assert is_valid("45RF") == False
    assert is_valid("D4FG") == False
    assert is_valid("$DFS4") == False
    assert is_valid("DFJ43") == True

def test_num():
    #numbers must be at the end, 0 cannot be first number
    assert is_valid("DF4JF") == False
    assert is_valid("DFG05") == False
    assert is_valid("DJT54") == True
    assert is_valid("DJT60") == True

def test_other():
    #apparently these are magic
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid(" 2") == False

if __name__ == "__main__":
    main()