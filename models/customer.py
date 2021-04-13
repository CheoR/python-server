class Customer():

    # special `self` parameter that every method on a class
    # needs as the first parameter.
    # {
    #     "email": "test@test.com",
    #     "name": "test test",
    #     "id": 9,
    #     "status": "Add status"
    # }

    def __init__(self, id, name, email, status):
        self.id = id
        self.name = name
        self.email = email
        self.status = status
