import sqlite3
import json

from models import Animal


ANIMALS = [
    {
        "id": 1,
        "name": "Peggy",
        "breed": "Pug",
        "customerId": 1,
        "locationId": 2,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Snippet",
        "breed": "Daschund",
        "customerId": 2,
        "locationId": 3,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Burrito",
        "breed": "Bulldog",
        "customerId": 3,
        "locationId": 4,
        "status": "Admitted"
    },
    {
        "id": 4,
        "name": "Bark",
        "breed": "Golden Retriever",
        "customerId": 4,
        "locationId": 5,
        "status": "Admitted"
    },
    {
        "id": 5,
        "name": "Gif",
        "breed": "Labador",
        "customerId": 5,
        "locationId": 6,
        "status": "Admitted"
    },
    {
        "id": 6,
        "name": "Bixo do Coco",
        "breed": "Chihuahua",
        "customerId": 1,
        "locationId": 2,
        "status": "Admitted"
    },
    {
        "name": "Pal",
        "breed": "Vicious teddy bear killer",
        "locationId": 3,
        "customerId": 2,
        "id": 7,
        "status": "Admitted"
    }
]


# def get_all_animals():
#     return ANIMALS


# def get_single_animal(id):
#     # Variable to hold the found animal, if it exists
#     requested_animal = None

#     for animal in ANIMALS:
#         if animal["id"] == id:
#             requested_animal = animal

#     return requested_animal


def create_animal(animal):
    # id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # get next id
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Append animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id, new_animal):
    # new animal - replacing entire object with user-given object
    # from Postman
    # Iterate ANIMALS list with enumerate()
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break


def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # .Row converts plain tuple into more useful object
        # .cursor is a reference to the db
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # For large datasets you can also iterate over the cursor itself.
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    # `json` package serializes list as JSON
    return json.dumps(animals)


def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        # a : reference to object ,good for shortening object's name
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])

        return json.dumps(animal.__dict__)
