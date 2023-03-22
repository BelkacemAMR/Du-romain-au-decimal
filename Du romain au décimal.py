def from_roman_numeral(numeral):
    value_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    value = 0
    last_digit_value = 0

    for roman_digit in numeral[::-1]:  # 1
        digit_value = value_map[roman_digit]

        if digit_value >= last_digit_value:  # 2
            value += digit_value
            last_digit_value = digit_value
        else:  # 3
            value -= digit_value

    return value