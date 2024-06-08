def egg_count(display_value):
    binary_representation = ''
    n = display_value
    while n > 0:
        binary_representation = str(n % 2) + binary_representation
        n = n // 2
    egg_count = 0
    for digit in binary_representation:
        if digit == '1':
            egg_count += 1
    return egg_count
