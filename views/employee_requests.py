EMPLOYEES = [{
        "id": 1,
        "name": "Alphonse Meron",
        "email": "ameron0@mashable.com",
    }, {
        "id": 2,
        "name": "Damara Pentecust",
        "email": "dpentecust1@apache.org",
    }, {
        "id": 3,
        "name": "Anna Bowton",
        "email": "abowton2@wisc.edu",
    }, {
        "id": 4,
        "name": "Hunfredo Drynan",
        "email": "hdrynan3@bizjournals.com",
    }, {
        "id": 5,
        "name": "Elmira Bick",
        "email": "ebick4@biblegateway.com",
    }, {
        "id": 6,
        "name": "Bernie Dreger",
        "email": "bdreger5@zimbio.com",
    }, {
        "id": 7,
        "name": "Rolando Gault",
        "email": "rgault6@google.com",
    }, {
        "id": 8,
        "name": "Tiffanie Tubby",
        "email": "ttubby7@intel.com",
    }, {
        "id": 9,
        "name": "Tomlin Cutill",
        "email": "tcutill8@marketwatch.com",
    }, {
        "id": 10,
        "name": "Arv Biddle",
        "email": "abiddle9@cafepress.com",
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
