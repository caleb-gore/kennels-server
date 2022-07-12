LOCATIONS = [
        { "id": 1, "name": "Pittsburgh"},
        { "id": 2, "name": "Minneapolis"},
        { "id": 3, "name": "Phoenix"},
        { "id": 4, "name": "Tucson"},
        { "id": 5, "name": "Denver"},
        { "id": 6, "name": "Boise"},
        { "id": 7, "name": "San Diego"},
        { "id": 8, "name": "Sarasota"},
        { "id": 9, "name": "White Plains"},
        { "id": 10, "name": "Chicago"}
    ]

def get_all_locations():
    """get entire LOCATIONS list

    Returns:
        list: all dictionaries in LOCATIONS
    """
    return LOCATIONS

def get_single_location(id):
    """get single dictionary from LOCATIONS

    Args:
        id (int): id of requested location

    Returns:
        dictionary: requested location
    """
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location
