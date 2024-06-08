def generate_seat_letters(number):
    seats = ['A', 'B', 'C', 'D']
    for i in range(number):
        yield seats[i % 4]


def generate_seats(number):
    seats = ['A', 'B', 'C', 'D']
    count = 0
    row = 1
    while count < number:
        if row == 13:
            row += 1
            continue
        for seat in seats:
            if count < number:
                yield f"{row}{seat}"
                count += 1
            else:
                break
        row += 1


def assign_seats(passengers):
    seats = ['A', 'B', 'C', 'D']
    count = 0
    row = 1
    while count < number:
        if row == 13:
            row += 1
            continue
        for seat in seats:
            if count < number:
                yield f"{row}{seat}"
                count += 1
            else:
                break
        row += 1


def assign_seats(passengers):
    seat_gene = generate_seats(len(passengers))
    seat_assignment = {}  
    for passenger in passengers:
        seat_assignment[passenger] = next(seat_gene)    
    return seat_assignment


def generate_codes(seat_numbers, flight_id):
    for seat in seat_numbers:
        code = f"{seat}{flight_id}".ljust(12, '0')
        yield code
