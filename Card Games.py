def get_rounds(number):
    return [number, number + 1, number + 2]
    

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    return number in rounds


def card_average(hand):
    total = sum(hand)
    number_of_cards = len(hand)
    avg = total / number_of_cards
    return avg   
        

def approx_average_is_average(hand):
    actual_average = sum(hand) / len(hand)
    first_last_average = (hand[0] + hand[-1]) / 2
    middle_index = len(hand) // 2
    median = hand[middle_index]
    return actual_average == first_last_average or actual_average == median


def average_even_is_average_odd(hand):
    return card_average(hand[::2]) == card_average(hand[1::2])


def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
