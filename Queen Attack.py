def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if not (0 <= int(digit) < input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")
    decimal_number = sum(int(digit) * input_base ** (len(digits) - 1 - i) for i, digit in enumerate(digits))
    output_digits = []
    while decimal_number > 0:
        remainder = decimal_number % output_base
        output_digits.insert(0, str(remainder))
        decimal_number //= output_base
    return output_digits or ['0']  
