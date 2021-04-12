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
