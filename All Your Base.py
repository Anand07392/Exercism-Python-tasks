def rebase(input_base, digits, output_base):
    if input_base <2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    base_10_number = 0
    for digit in digits:
        base_10_number = base_10_number * input_base + digit
    if base_10_number == 0:
        return [0]
    output_digits = []
    while base_10_number > 0:
        output_digits.append(base_10_number % output_base)
        base_10_number //= output_base    
    output_digits.reverse()
    return output_digits
