COLOR_CODES = {"black": 0, 
               "brown": 1, 
               "red": 2, 
               "orange": 3, 
               "yellow": 4, 
               "green": 5, 
               "blue": 6, 
               "violet": 7, 
               "grey": 8, 
               "white": 9}
def value(colors):
    first_color = colors[0].lower()
    second_color = colors[1].lower()
    first_value = COLOR_CODES[first_color]
    second_value = COLOR_CODES[second_color]
    resistance_value = int(f"{first_value}{second_value}")
    return resistance_value
