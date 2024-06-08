COLOR_TO_VALUE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def color_code(color):
    if color in COLOR_TO_VALUE:
        return COLOR_TO_VALUE[color]
    else:
        raise ValueError(f"Invalid color: {color}")
      
def colors():
    return COLORS
