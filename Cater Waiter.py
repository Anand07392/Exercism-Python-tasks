from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)
def clean_ingredients(dish_name, dish_ingredients):
    deduplicated_ingredients = set(dish_ingredients)
    return dish_name, deduplicated_ingredients


def check_drinks(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        if ingredient.lower() in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    dish_ingredients_lower = {ingredient.lower() for ingredient in dish_ingredients}
    if dish_ingredients_lower.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif dish_ingredients_lower.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif dish_ingredients_lower.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif dish_ingredients_lower.issubset(KETO):
        return f"{dish_name}: KETO"
    elif dish_ingredients_lower.issubset(OMNIVORE):
        return f"{dish_name}: OMNIVORE"
    else:
        return f"{dish_name}: Unknown category"


def tag_special_ingredients(dish):
    dish_name, ingredients = dish
    special_ingredients = set(ingredient for ingredient in ingredients if ingredient in SPECIAL_INGREDIENTS)
    return (dish_name, special_ingredients)


def compile_ingredients(dishes):
    all_ingredients = set()
    for dish in dishes:
        all_ingredients.update(dish)
    return all_ingredients


def separate_appetizers(dishes, appetizers):
    dish_set = set(dishes)
    appetizer_set = set(appetizers)
    main_dishes = dish_set.difference(appetizer_set)
    return list(main_dishes)


def singleton_ingredients(dishes, intersection):
    all_ingredients = set()
    for dish in dishes:
        all_ingredients.update(dish)
    singleton_ingredients = all_ingredients - intersection
    return singleton_ingredients
