class Location():

    # special `self` parameter that every method on a class
    # needs as the first parameter.
    # {
    #     "name": "delete this location",
    #     "address": "location to delte",
    #     "id": 8,
    #     "status": "Add status"
    # }

    def __init__(self, id, name, address, status):
        self.id = id
        self.name = name
        self.address = address
        self.status = status
