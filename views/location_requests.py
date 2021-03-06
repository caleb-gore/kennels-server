LOCATIONS = [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
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

def create_location(location):
    """create new location dictionary

    Args:
        location (dictionary): new dictionary

    Returns:
        dictionary: the newly created dictionary
    """
    # Get the id value of the last animal in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    """remove location dictionary from LOCATIONS list

    Args:
        id (int): id of dictionary to be deleted
    """
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    """update the LOCATIONS dictionary with new data

    Args:
        id (int): id of dictionary
        new_location (dict): updated dictionary
    """
    # Iterate the LOCATIONS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break
