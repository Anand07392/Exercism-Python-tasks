def square_root(n):
    if n < 1:
        raise ValueError("Input must be a natural number (positive integer).")
    guess = n / 2.0
    tolerance = 1e-6
    while True:
        new_guess = (guess + n / guess) / 2.0
        if abs(new_guess - guess) < tolerance:
            break
        guess = new_guess
    return int(guess)
