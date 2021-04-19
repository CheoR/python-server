class Animal():

    # special `self` parameter that every method on a class
    # needs as the first parameter.
    # {
    #     "id": 3,
    #     "name": "Burrito",
    #     "breed": "Bulldog",
    #     "customerId": 3,
    #     "locationId": 4,
    #     "status": "Admitted"
    # }
    def __init__(self, id, name, breed, customer_id, location_id="", status=""):
        self.id = id
        self.name = name
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
