EMPLOYEES = [
    {
        "id": 1,
        "name": "Peggy",
        "job": "Professional Dog Snuggles",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Cat Lady",
        "job": "Picks up cat poop",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Mage",
        "job": "Eats poop",
        "locationId": 2
    },
    {
        "id": 4,
        "name": "Hobo Jack",
        "job": "Doesn't actually work here, just hangs out here.",
        "locationId": 2
    },
    {
        "id": 5,
        "name": "Drifter Jeff",
        "job": "Hobo Jack's friend",
        "locationId": 3
    },
    {
        "id": 6,
        "name": "Charlie",
        "job": "Horse without a liver.",
        "locationId": 3
    },
    {
        "name": "Sunny",
        "job": "Ray Of Happiness",
        "locationId": 2,
        "id": 7
    },
    {
        "name": "mr delete",
        "job": "deleting stuff",
        "locationId": 2,
        "id": 8
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
