EMPLOYEES = [{
        "id": 1,
        "name": "Alphonse Meron",
        "email": "ameron0@mashable.com",
        "locationId": 1
    }, {
        "id": 2,
        "name": "Damara Pentecust",
        "email": "dpentecust1@apache.org",
        "locationId": 3
    }, {
        "id": 3,
        "name": "Anna Bowton",
        "email": "abowton2@wisc.edu",
        "locationId": 4
    }, {
        "id": 4,
        "name": "Hunfredo Drynan",
        "email": "hdrynan3@bizjournals.com",
        "locationId": 5
    }, {
        "id": 5,
        "name": "Elmira Bick",
        "email": "ebick4@biblegateway.com",
        "locationId": 6
    }, {
        "id": 6,
        "name": "Bernie Dreger",
        "email": "bdreger5@zimbio.com",
        "locationId": 7
    }, {
        "id": 7,
        "name": "Rolando Gault",
        "email": "rgault6@google.com",
        "locationId": 8
    }, {
        "id": 8,
        "name": "Tiffanie Tubby",
        "email": "ttubby7@intel.com",
        "locationId": 9
    }, {
        "id": 9,
        "name": "Tomlin Cutill",
        "email": "tcutill8@marketwatch.com",
        "locationId": 10
    }, {
        "id": 10,
        "name": "Arv Biddle",
        "email": "abiddle9@cafepress.com",
        "locationId": 11
    }]

def get_all_employees():
    """get entire EMPLOYEES list

    Returns:
        list: all dictionaries in EMPLOYEES
    """
    return EMPLOYEES

def get_single_employee(id):
    """get single dictionary from EMPLOYEES list

    Args:
        id (int): id of requested employee

    Returns:
        dictionary: requested employee
    """
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee

def create_employee(employee):
    """create new employee dictionary

    Args:
        employee (dictionary): new dictionary

    Returns:
        dictionary: the newly created dictionary
    """
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee

def delete_employee(id):
    """remove employee dictionary from EMPLOYEES list

    Args:
        id (int): id of dictionary to be deleted
    """
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the EMPLOYEES list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    """update the EMPLOYEES dictionary with new data

    Args:
        id (int): id of dictionary
        new_employee (dict): updated dictionary
    """
    # Iterate the EMPLOYEES list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break
