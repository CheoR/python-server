import sqlite3
import json

from models import Customer


# CUSTOMERS = [
#     {
#         "id": 7,
#         "name": "Hannah Hall",
#         "address": "7002 Chestnut Ct",
#         "email": "hannah.hall@gmail.com",
#         "status": "Add status"
#     },
#     {
#         "id": 1,
#         "name": "Customer 1",
#         "address": "123 W Fake St",
#         "email": "customer1@gmail.com",
#         "status": "Add status"
#     },
#     {
#         "id": 2,
#         "name": "Customer 2",
#         "address": "456 Also Fake Rd.",
#         "email": "customer2@gmail.com",
#         "status": "Add status"
#     },
#     {
#         "id": 3,
#         "name": "Customer 3",
#         "address": "789 Fake Way",
#         "email": "customer3@gmail.com",
#         "status": "Add status"
#     },
#     {
#         "id": 4,
#         "name": "Customer 4",
#         "address": "1234 Fake Blvd",
#         "email": "customer4@gmail.com",
#         "status": "Add status"
#     },
#     {
#         "id": 5,
#         "name": "Customer 5",
#         "address": "5678 Fake Ct",
#         "email": "customer5@gmail.com",
#         "status": "Add status"
#     },
#     {
#         "id": 6,
#         "name": "Customer 6",
#         "address": "123 E Fake St",
#         "email": "customer6@gmail.com",
#         "status": "Add status"
#     },
#     {
#         "email": "test.name@gmail.com",
#         "name": "test name",
#         "id": 8,
#         "status": "Add status"
#     },
#     {
#         "email": "test@test.com",
#         "name": "test test",
#         "id": 9,
#         "status": "Add status"
#     }
# ]


# def get_all_customers():
#     return CUSTOMERS


# # Function with a single parameter
# def get_single_customer(id):
#     # Variable to hold the found customer, if it exists
#     requested_customer = None

#     # Iterate the customerS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for customer in CUSTOMERS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         print(f"id is: {id}")
#         if customer["id"] == id:
#             requested_customer = customer

#     return requested_customer


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


def update_customer(id, new_customer):
    # new customer - replacing entire object with user-given object
    # from Postman
    # Iterate CUSTOMERS list with enumerate()
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break


def get_all_customers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # .Row converts plain tuple into more useful object
        # .cursor is a reference to the db
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # For large datasets you can also iterate over the cursor itself.
        for row in dataset:

            # Create an customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Customer class above.
            customer = Customer(row['id'], row['name'], row['address'],
                                row['email'], row['password'])

            customers.append(customer.__dict__)

    # `json` package serializes list as JSON
    return json.dumps(customers)


def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        # a : reference to object ,good for shortening object's name
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'], data['password'])

        return json.dumps(customer.__dict__)


def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address
        from customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
