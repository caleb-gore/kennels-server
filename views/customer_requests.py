CUSTOMERS =  [{
        "id": 1,
        "name": "Dianemarie Hartness",
        "walkerId": 3
    }, {
        "id": 2,
        "name": "Christoph Fosdyke",
        "walkerId": 10
    }, {
        "id": 3,
        "name": "Rocket",
        "walkerId": 7
    }, {
        "id": 4,
        "name": "Ebony",
        "walkerId": 3
    }, {
        "id": 5,
        "name": "Scotty",
        "walkerId": 8
    }, {
        "id": 6,
        "name": "Mac",
        "walkerId": 2
    }, {
        "id": 7,
        "name": "Oreo",
        "walkerId": 5
    }, {
        "id": 8,
        "name": "Sassy",
        "walkerId": 1
    }, {
        "id": 9,
        "name": "Salem",
        "walkerId": 9
    }, {
        "id": 10,
        "name": "Panda",
        "walkerId": 7
    }]

def get_all_customers():
    """get entire CUSTOMERS list

    Returns:
        list: all dictionaries in CUSTOMERS
    """
    return CUSTOMERS

def get_single_customer(id):
    """get single dictionary from CUSTOMERS list

    Args:
        id (int): id of requested customer

    Returns:
        dictionary: requested customer
    """
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer
