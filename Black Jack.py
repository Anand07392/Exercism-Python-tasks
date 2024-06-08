def value_of_card(card):
    if card == 'A':
        return 1
    elif card in ['J', 'Q', 'K']:
        return 10
    else:
        return int(card)


def higher_card(card_one, card_two):
    card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    value_one = card_values.get(card_one, None)
    value_two = card_values.get(card_two, None)
    if value_one is None or value_two is None:
        return "Invalid card value"
    elif value_one > value_two:
        return card_one
    elif value_one < value_two:
        return card_two
    else:
        return card_one, card_two
        

def value_of_ace(card_one, card_two):
    if card_one in ['J', 'Q', 'K']:
        value_one = 10
    elif card_one == 'A':
        value_one = 11
    else:
        value_one = int(card_one)  
    if card_two in ['J', 'Q', 'K']:
        value_two = 10
    elif card_two == 'A':
        value_two = 11
    else:
        value_two = int(card_two)
    ace_in_hand = card_one == 'A' or card_two == 'A'
    total_value = value_one + value_two
    if ace_in_hand:
        return 1  
    if total_value + 11 <= 21:
        return 11 
    else:
        return 1 


def is_blackjack(card_one, card_two):
    ten_cards = ['10', 'J', 'Q', 'K']
    if (card_one == 'A' and card_two in ten_cards) or (card_two == 'A' and card_one in ten_cards):
        return True
    return False
        
     
def can_split_pairs(card_one, card_two):
    if card_one == card_two:
        return True
    face_cards = ['J', 'Q', 'K']
    if (card_one in face_cards) and (card_two in face_cards):
        return True
    return False


def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) >= 9 and value_of_card(card_one) + value_of_card(
            card_two) <= 11:
        return True
    return False


    
