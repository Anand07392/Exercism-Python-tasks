def bake_time_remaining(time_baked):
  return EXPECTED_BAKE_TIME-time_baked

def preparation_time_in_minutes(number_of_layers):
    preparation_time=2
    return number_of_layers*preparation_time

def  elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time PREPARATION_TIME_PER_LAYER = 2

def preparation_time_in_minutes(number_of_layers):
  preparation_time = number_of_layers * PREPARATION_TIME_PER_LAYER
  return preparation_time
