class Customer():

    # special `self` parameter that every method on a class
    # needs as the first parameter.
    # {
    #     "email": "test@test.com",
    #     "name": "test test",
    #     "id": 9,
    #     "status": "Add status"
    # }

    # when create some Customer instances to send back the client,
    #  sending the password in the response is a bad idea.
    #  There's no reason to send the email in the case since the client obviously already has the email address to reference.
    def __init__(self, id, name, address, email="", password=""):  # , status):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        # self.status = status
