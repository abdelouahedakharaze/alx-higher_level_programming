#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or 
    roman_string is None:
        return 0
    convert_table = {"I": 1, "V": 5, "X": 10, "L": 50,
                     "C": 100, "D": 500, "M": 1000}
    rslt = 0
    valp = 0

    for numeral in roman_string:
        value = convert_table.get(numeral, 0)

        if value > valp:
            rslt += value - 2 * valp
        else:
            rslt += value

        valp = value

    return rslt
