import sqlite3
import json

from models import Animal
from models import Location
from models import Customer


# ANIMALS = [
#     {
#         "id": 1,
#         "name": "Peggy",
#         "breed": "Pug",
#         "customerId": 1,
#         "locationId": 2,
#         "status": "Admitted"
#     },
#     {
#         "id": 2,
#         "name": "Snippet",
#         "breed": "Daschund",
#         "customerId": 2,
#         "locationId": 3,
#         "status": "Admitted"
#     },
#     {
#         "id": 3,
#         "name": "Burrito",
#         "breed": "Bulldog",
#         "customerId": 3,
#         "locationId": 4,
#         "status": "Admitted"
#     },
#     {
#         "id": 4,
#         "name": "Bark",
#         "breed": "Golden Retriever",
#         "customerId": 4,
#         "locationId": 5,
#         "status": "Admitted"
#     },
#     {
#         "id": 5,
#         "name": "Gif",
#         "breed": "Labador",
#         "customerId": 5,
#         "locationId": 6,
#         "status": "Admitted"
#     },
#     {
#         "id": 6,
#         "name": "Bixo do Coco",
#         "breed": "Chihuahua",
#         "customerId": 1,
#         "locationId": 2,
#         "status": "Admitted"
#     },
#     {
#         "name": "Pal",
#         "breed": "Vicious teddy bear killer",
#         "locationId": 3,
#         "customerId": 2,
#         "id": 7,
#         "status": "Admitted"
#     }
# ]


# def get_all_animals():
#     return ANIMALS


# def get_single_animal(id):
#     # Variable to hold the found animal, if it exists
#     requested_animal = None

#     for animal in ANIMALS:
#         if animal["id"] == id:
#             requested_animal = animal

#     return requested_animal


# def create_animal(animal):
#     # id value of the last animal in the list
#     max_id = ANIMALS[-1]["id"]

#     # get next id
#     new_id = max_id + 1

#     # Add an `id` property to the animal dictionary
#     animal["id"] = new_id

#     # Append animal dictionary to the list
#     ANIMALS.append(animal)

#     # Return the dictionary with `id` property added
#     return animal


def create_animal(new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Animal
            ( name, breed, status, location_id, customer_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_animal["name"], new_animal["breed"],
              new_animal["status"], new_animal["location_id"],
              new_animal["customer_id"], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_animal["id"] = id

    return json.dumps(new_animal)


# def delete_animal(id):
#     # Initial -1 value for animal index, in case one isn't found
#     animal_index = -1

#     # Iterate the ANIMALS list, but use enumerate() so that you
#     # can access the index value of each item
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Store the current index.
#             animal_index = index

#     # If the animal was found, use pop(int) to remove it from list
#     if animal_index >= 0:
#         ANIMALS.pop(animal_index)


# def update_animal(id, new_animal):
#     # new animal - replacing entire object with user-given object
#     # from Postman
#     # Iterate ANIMALS list with enumerate()
#     for index, animal in enumerate(ANIMALS):
#         if animal["id"] == id:
#             # Found the animal. Update the value.
#             ANIMALS[index] = new_animal
#             break


def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:

        # .Row converts plain tuple into more useful object
        # .cursor is a reference to the db
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        # In case instace, a JOIN query to embed location data
        # into an animal instance.
        db_cursor.execute("""
            SELECT
                a.id,
                a.name,
                a.breed,
                a.status,
                a.location_id,
                a.customer_id,
                l.id AS location_id,
                l.name AS location_name,
                l.address AS location_address,
                l.status AS location_status,
                c.id As customer_id,
                c.name As customer_name,
                c.address As customer_address
            FROM Animal a
            JOIN Location l
            ON l.id = a.location_id
            JOIN Customer c
            ON c.id = a.customer_id
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
                            row['customer_id'], row['location_id'],
                            row['status'])

            # Location instance from the current row
            location = Location(row['location_id'], row['location_name'],
                                row['location_address'], row['location_status'])

            customer = Customer(
                row['customer_id'], row['customer_name'], row['customer_address'])

            # Add the dictionary representation of the location to the animal
            animal.location = location.__dict__
            animal.customer = customer.__dict__

            # Add the dictionary representation of the animal to the list
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
                        data['customer_id'], data['location_id'],
                        data['status'])

        return json.dumps(animal.__dict__)


def get_animals_by_location(location):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id
        FROM animal a
        WHERE a.location_id = ?
        """, (location, ))

        animals = []

        data = db_cursor.fetchall()
        for row in data:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['customer_id'], row['status'])
            animals.append(animal.__dict__)
        return json.dumps(animals)


def get_animals_by_status(status):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        WHERE a.status = ?
        """, (status, ))

        animals = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['customer_id'], row['location_id'])

            animals.append(animal.__dict__)

    return json.dumps(animals)


def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM animal
        WHERE id = ?
        """, (id, ))


def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        # When a PUT request to change the values of a current row in your database,
        # it will be sending the ENTIRE representation.
        # Not just the one field that it wants to change.
        # Therefore, you must update each field for the resource based on what the client
        # sends you since you can't possibly know what has changed.
        db_cursor.execute("""
        UPDATE Animal
            SET
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['location_id'],
              new_animal['customer_id'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
