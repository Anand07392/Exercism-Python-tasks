def get_coordinate(record):
    s=record[1]
    return s


def convert_coordinate(coordinate):
    s=tuple(coordinate)
    return s


def compare_records(azara_record, rui_record):
    azara_coordinate = azara_record[1]
    rui_coordinate = rui_record[1]
    azara_numeric = ''.join(filter(str.isdigit, azara_coordinate))
    azara_alpha = ''.join(filter(str.isalpha, azara_coordinate))
    normalized_azara_coordinate = (azara_numeric, azara_alpha)
    rui_numeric, rui_alpha = rui_coordinate
    normalized_rui_coordinate = (rui_numeric, rui_alpha)
    return normalized_azara_coordinate == normalized_rui_coordinate


def create_record(azara_record, rui_record):
    azara_coordinate = azara_record[1]
    rui_coordinate = rui_record[1]
    azara_numeric = ''.join(filter(str.isdigit, azara_coordinate))
    azara_alpha = ''.join(filter(str.isalpha, azara_coordinate))
    normalized_azara_coordinate = (azara_numeric, azara_alpha)
    rui_numeric, rui_alpha = rui_coordinate
    normalized_rui_coordinate = (rui_numeric, rui_alpha)
    if normalized_azara_coordinate == normalized_rui_coordinate:
        return (azara_record[0], azara_record[1], rui_record[0], rui_record[1], rui_record[2])
    else:
        return "not a match"


def clean_up(combined_record_group):
    clean_record = ""
    for record in combined_record_group:
        clean_record += str(record[:1] + record[2:]) + "\n"
    return clean_record
