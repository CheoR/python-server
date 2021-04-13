EMPLOYEES = [
    {
        "id": 1,
        "name": "Peggy",
        "job": "Professional Dog Snuggles",
        "locationId": 1,
        "status": "Add status"
    },
    {
        "id": 2,
        "name": "Cat Lady",
        "job": "Picks up cat poop",
        "locationId": 1,
        "status": "Add status"
    },
    {
        "id": 3,
        "name": "Mage",
        "job": "Eats poop",
        "locationId": 2,
        "status": "Add status"
    },
    {
        "id": 4,
        "name": "Hobo Jack",
        "job": "Doesn't actually work here, just hangs out here.",
        "locationId": 2,
        "status": "Add status"
    },
    {
        "id": 5,
        "name": "Drifter Jeff",
        "job": "Hobo Jack's friend",
        "locationId": 3,
        "status": "Add status"
    },
    {
        "id": 6,
        "name": "Charlie",
        "job": "Horse without a liver.",
        "locationId": 3,
        "status": "Add status"
    },
    {
        "name": "Sunny",
        "job": "Ray Of Happiness",
        "locationId": 2,
        "id": 7,
        "status": "Add status"
    },
    {
        "name": "mr delete",
        "job": "deleting stuff",
        "locationId": 2,
        "id": 8,
        "status": "Add status"
    }
]


def get_all_employees():
    return EMPLOYEES
# Function with a single parameter


def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


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
