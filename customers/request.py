CUSTOMERS = [
    {
        "id": 7,
        "name": "Hannah Hall",
        "address": "7002 Chestnut Ct",
        "email": "hannah.hall@gmail.com"
    },
    {
        "id": 1,
        "name": "Customer 1",
        "address": "123 W Fake St",
        "email": "customer1@gmail.com"
    },
    {
        "id": 2,
        "name": "Customer 2",
        "address": "456 Also Fake Rd.",
        "email": "customer2@gmail.com"
    },
    {
        "id": 3,
        "name": "Customer 3",
        "address": "789 Fake Way",
        "email": "customer3@gmail.com"
    },
    {
        "id": 4,
        "name": "Customer 4",
        "address": "1234 Fake Blvd",
        "email": "customer4@gmail.com"
    },
    {
        "id": 5,
        "name": "Customer 5",
        "address": "5678 Fake Ct",
        "email": "customer5@gmail.com"
    },
    {
        "id": 6,
        "name": "Customer 6",
        "address": "123 E Fake St",
        "email": "customer6@gmail.com"
    },
    {
        "email": "test.name@gmail.com",
        "name": "test name",
        "id": 8
    },
    {
        "email": "test@test.com",
        "name": "test test",
        "id": 9
    }
]


def get_all_customers():
    return CUSTOMERS


# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the customerS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the customerS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
