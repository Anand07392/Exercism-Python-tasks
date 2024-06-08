def get_list_of_wagons(*s):
    return list(s)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    wagons_to_move = each_wagons_id[:2]
    each_wagons_id = each_wagons_id[2:] + wagons_to_move
    locomotive_index = each_wagons_id.index(1)
    modified_list = each_wagons_id[:locomotive_index + 1] + missing_wagons + each_wagons_id[locomotive_index + 1:] 
    return modified_list


def add_missing_stops(routing, **kwargs):
    stops = []
    for key, value in kwargs.items():
        if isinstance(value, dict):
            sorted_stops = sorted(value.items(), key=lambda item: item[0])
            stops.extend([stop for _, stop in sorted_stops])
        else:
            stops.append(value)
    routing['stops'] = stops
    return routing


def extend_route_information(route, more_route_information):
    consolidated_route = {**route, **more_route_information}
    return consolidated_route


def fix_wagon_depot(wagons_rows):
    column1 = []
    column2 = []
    column3 = []
    for row in wagons_rows:
        wagon1, color1 = row[0]
        wagon2, color2 = row[1]
        wagon3, color3 = row[2]
        column1.append((wagon1, color1))
        column2.append((wagon2, color2))
        column3.append((wagon3, color3))
    return [column1, column2, column3]
