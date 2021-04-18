import sqlite3
import json

from models import Location


LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 E Johnson Pike",
        "status": "Add status"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 W Emory Drive",
        "status": "Add status"
    },
    {
        "id": 3,
        "name": "Nashville East",
        "address": "8422 N Johnson Pike",
        "status": "Add status"
    },
    {
        "id": 4,
        "name": "Nashville West",
        "address": "209 S Emory Drive",
        "status": "Add status"
    },
    {
        "id": 5,
        "name": "Nashville North",
        "address": "8422 N Johnson Pike",
        "status": "Add status"
    },
    {
        "id": 6,
        "name": "Nashville South",
        "address": "209 S Emory Drive",
        "status": "Add status"
    },
    {
        "name": "testloc1",
        "address": "123 fake street, nashville tn",
        "id": 7,
        "status": "Add status"
    },
    {
        "name": "delete this location",
        "address": "location to delte",
        "id": 8,
        "status": "Add status"
    }
]


# def get_all_locations():
#     return LOCATIONS


# def get_single_location(id):
#     # Variable to hold the found location, if it exists
#     requested_location = None

#     # Iterate the LOCATIONS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for location in LOCATIONS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if location["id"] == id:
#             requested_location = location

#     return requested_location


def create_location(location):
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the location dictionary
    location["id"] = new_id

    # Add the location dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location


def delete_location(id):
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the locationS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, new_location):
    # new location - replacing entire object with user-given object
    # from Postman
    # Iterate locationS list with enumerate()
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break


def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # .Row converts plain tuple into more useful object
        # .cursor is a reference to the db
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address,
            l.status
        FROM location l
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # For large datasets you can also iterate over the cursor itself.
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Location class above.
            location = Location(row['id'], row['name'],
                                row['address'], row['status'])

            locations.append(location.__dict__)

    # `json` package serializes list as JSON
    print("I should ont rint for single item")
    return json.dumps(locations)


def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        # l : reference to object ,good for shortening object's name
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address,
            l.status
        FROM location l
        WHERE l.id = ?
        """, (id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an location instance from the current row
        location = Location(data['id'], data['name'],
                            data['address'], data['status'])

        return json.dumps(location.__dict__)
