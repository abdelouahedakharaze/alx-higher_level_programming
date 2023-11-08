#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rtble = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rls = 0

    for i in range(len(roman_string)):
        if rtble.get(roman_string[i], 0) == 0:
            return 0

        if (
            i != (len(roman_string) - 1)
            and rtble[roman_string[i]] < rtble[roman_string[i + 1]]
        ):
            rls += rtble[roman_string[i]] * -1

        else:
            rls += rtble[roman_string[i]]
    return rls
