
class AddressInvalid(Exception):
    def __init__(self, address, message="This address is not valid."):
        self.message = message
        super().__init__(self.message)

class BlockInvalid(Exception):
    def __init__(self, address, message="This block is not valid, are you sure you are sending the right variable?"):
        self.message = message
        super().__init__(self.message)
