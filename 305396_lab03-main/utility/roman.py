def int_to_roman(num):
    if not isinstance(num, int) or not 0 < num < 4000:
        raise ValueError("Input must be an integer between 1 and 3999")

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ''
    for value, symbol in roman_numerals.items():
        while num >= value:
            result += symbol
            num -= value

    return result

