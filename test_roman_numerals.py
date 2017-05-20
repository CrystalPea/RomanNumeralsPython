import pytest
from roman_numerals import convert

@pytest.mark.parametrize('number,numeral', [
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
    (50, "L"),
    (40, "XL"),
    (100, "C"),
    (7, "VII"),
    (14, "XIV"),
    (88, "LXXXVIII"),
    (69, "LXIX"),
    (96, "XCVI"),
    (420, "CDXX"),
    (555, "DLV"),
    (911, "CMXI"),
    (2017, "MMXVII")
])
def test_convert_number(number, numeral):
    assert convert(number) == numeral
