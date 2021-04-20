import sqlite3
import json

from models import Employee
from models import Location

# EMPLOYEES = [
#     {
#         "id": 1,
#         "name": "Peggy",
#         "job": "Professional Dog Snuggles",
#         "locationId": 1,
#         "status": "Add status"
#     },
#     {
#         "id": 2,
#         "name": "Cat Lady",
#         "job": "Picks up cat poop",
#         "locationId": 1,
#         "status": "Add status"
#     },
#     {
#         "id": 3,
#         "name": "Mage",
#         "job": "Eats poop",
#         "locationId": 2,
#         "status": "Add status"
#     },
#     {
#         "id": 4,
#         "name": "Hobo Jack",
#         "job": "Doesn't actually work here, just hangs out here.",
#         "locationId": 2,
#         "status": "Add status"
#     },
#     {
#         "id": 5,
#         "name": "Drifter Jeff",
#         "job": "Hobo Jack's friend",
#         "locationId": 3,
#         "status": "Add status"
#     },
#     {
#         "id": 6,
#         "name": "Charlie",
#         "job": "Horse without a liver.",
#         "locationId": 3,
#         "status": "Add status"
#     },
#     {
#         "name": "Sunny",
#         "job": "Ray Of Happiness",
#         "locationId": 2,
#         "id": 7,
#         "status": "Add status"
#     },
#     {
#         "name": "mr delete",
#         "job": "deleting stuff",
#         "locationId": 2,
#         "id": 8,
#         "status": "Add status"
#     }
# ]


# def get_all_employees():
#     return EMPLOYEES
# # Function with a single parameter


# def get_single_employee(id):
#     # Variable to hold the found employee, if it exists
#     requested_employee = None

#     # Iterate the EMPLOYEES list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for employee in EMPLOYEES:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if employee["id"] == id:
#             requested_employee = employee

#     return requested_employee


# def create_employee(employee):
#     # Get the id value of the last employee in the list
#     max_id = EMPLOYEES[-1]["id"]

#     # Add 1 to whatever that number is
#     new_id = max_id + 1

#     # Add an `id` property to the employee dictionary
#     employee["id"] = new_id

#     # Add the employee dictionary to the list
#     EMPLOYEES.append(employee)

#     # Return the dictionary with `id` property added
#     return employee


def create_employee(new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO employee
            ( name, address, location_id )
        VALUES
            ( ?, ?, ? );
        """, (new_employee["name"], new_employee["address"], new_employee["location_id"], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the employee dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_employee["id"] = id

    return json.dumps(new_employee)


def delete_employee(id):
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the employeeS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    # new employee - replacing entire object with user-given object
    # from Postman
    # Iterate employeeS list with enumerate()
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break


def get_all_employees():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # .Row converts plain tuple into more useful object
        # .cursor is a reference to the db
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        # Aliases defined in Select not respected in ON.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            l.id AS location_id,
            l.name AS location_name,
            l.address AS location_address,
            l.status AS location_status
        FROM Employee e
        JOIN Location l
        ON e.location_id = l.id
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # For large datasets you can also iterate over the cursor itself.
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(row['id'], row['name'],
                                row['address'], row['location_id'])
            location = Location(row['location_id'], row['location_name'],
                                row['location_address'], row['location_status'])

            employee.location = location.__dict__
            employees.append(employee.__dict__)

    # `json` package serializes list as JSON
    return json.dumps(employees)


def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        # a : reference to object ,good for shortening object's name
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'],
                            data['address'], data['location_id'])

        return json.dumps(employee.__dict__)


def get_employees_by_location(location):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM employee e
        WHERE e.location_id = ?
        """, (location, ))

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['address'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
