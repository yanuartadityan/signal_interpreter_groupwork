from example_1_get_full_name import get_full_name

def test_full_name():
    assert get_full_name("John", "Smith") == "John Smith"
    assert get_full_name("H.", "Sumarni") == "H. Sumarni"