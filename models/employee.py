class Employee():

    # special `self` parameter that every method on a class
    # needs as the first parameter.
    # {
    #     "name": "mr delete",
    #     "job": "deleting stuff",
    #     "locationId": 2,
    #     "id": 8,
    #     "status": "Add status"
    # }

    # def __init__(self, id, name, job, location_id, status):
    #     self.id = id
    #     self.name = name
    #     self.job = job
    #     self.status = status
    #     self.location_id = location_id

    def __init__(self, id, name, address, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
