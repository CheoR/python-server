ANIMALS = [
    {
        "id": 1,
        "name": "Peggy",
        "breed": "Pug",
        "customerId": 1,
        "locationId": 2
    },
    {
        "id": 2,
        "name": "Snippet",
        "breed": "Daschund",
        "customerId": 2,
        "locationId": 3
    },
    {
        "id": 3,
        "name": "Burrito",
        "breed": "Bulldog",
        "customerId": 3,
        "locationId": 4
    },
    {
        "id": 4,
        "name": "Bark",
        "breed": "Golden Retriever",
        "customerId": 4,
        "locationId": 5
    },
    {
        "id": 5,
        "name": "Gif",
        "breed": "Labador",
        "customerId": 5,
        "locationId": 6
    },
    {
        "id": 6,
        "name": "Bixo do Coco",
        "breed": "Chihuahua",
        "customerId": 1,
        "locationId": 2
    },
    {
        "name": "Pal",
        "breed": "Vicious teddy bear killer",
        "locationId": 3,
        "customerId": 2,
        "id": 7
    }
]


def get_all_animals():
    return ANIMALS


def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


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
