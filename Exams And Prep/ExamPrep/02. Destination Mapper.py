import re

def calculate_travel_points(locations):
    pattern = r"(\=|\/)([A-Z][A-Z-a-z]{2,})\1"
    valid_locations = []
    travel_point = 0
    result = re.finditer(pattern, locations)
    for location in result:
        valid_locations.append(location.group(2))
        travel_point += len(location.group(2))
    print(f'Destinations: {", ".join(valid_locations)}\nTravel Points: {travel_point}')

locations = input()

calculate_travel_points(locations)
