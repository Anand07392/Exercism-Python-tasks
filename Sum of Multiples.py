def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    for multiple in multiples:
        if multiple == 0:
            continue
        current = multiple
        while current < limit:
            unique_multiples.add(current)
            current += multiple
    return sum(unique_multiples)
