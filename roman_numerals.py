roman_numerals = [
    {1000: "M"},
    {900: "CM"},
    {500: "D"},
    {400: "CD"},
    {100: "C"},
    {90: "XC"},
    {50: "L"},
    {40: "XL"},
    {10: "X"},
    {9: "IX"},
    {5: "V"},
    {4: "IV"},
    {1: "I"}
]

def convert(integer, numerals=roman_numerals):
    result = ""
    for pair in numerals:
        for key in pair:
            while integer >= key:
                if integer >= key:
                    result += pair[key]
                    integer -= key
    return result
