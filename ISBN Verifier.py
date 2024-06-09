def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    if not (isbn[:9].isdigit() and (isbn[9].isdigit() or isbn[9] == 'X')):
        return False
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (10 - i)
    if isbn[9] == 'X':
        total += 10
    else:
        total += int(isbn[9])
    return total % 11 == 0
