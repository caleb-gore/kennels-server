CUSTOMERS =  [{
            "id": 1,
            "name": "Hannah Hall",
            "address": "7002 Chestnut Ct"
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

def create_customer(customer):
    """create new customer dictionary

    Args:
        customer (dictionary): new dictionary

    Returns:
        dictionary: the newly created dictionary
    """
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    """remove customer dictionary from CUSTOMERS list

    Args:
        id (int): id of dictionary to be deleted
    """
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """update the CUSTOMERS dictionary with new data

    Args:
        id (int): id of dictionary
        new_customer (dict): updated dictionary
    """
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break
