class Request():

    def __init__(self, request_number, product, payment_method, description, cellphone) -> None:
        self.request_number = request_number
        self.product = product
        self.payment_method = payment_method
        self.description = description
        self.cellphone = cellphone