class Error(Exception):
    """Base class for other exceptions"""
    pass


class AddressInvalid(Exception):
    def __init__(self, address, message="This address is not valid."):
        self.message = message
        super().__init__(self.message)


class BlockInvalid(Exception):
    def __init__(self, address, message="This block is not valid, are you sure you are sending the right variable?"):
        self.message = message
        super().__init__(self.message)


class InvalidServerResponseHTML(Exception):
    def __init__(self, message="Received invalid response from node (type HTML, expected JSON)"):
        self.message = message
        super().__init__(self.message)


class CannotConnect(Exception):
    def __init__(self, message="Failed to establish a new connection to the node"):
        self.message = message
        super().__init__(self.message)


class ActionNotSupported(Exception):
    def __init__(self, message="Node does not support the requested function"):
        self.message = message
        super().__init__(self.message)


class WalletNotFound(Exception):
    def __init__(self, message="Wallet not found"):
        self.message = message
        super().__init__(self.message)


class InvalidBlockHash(Exception):
    def __init__(self, message="Invalid block hash."):
        self.message = message
        super().__init__(self.message)


class UnknownError(Exception):
    def __init__(self, message="The node returned an unknown error"):
        self.message = message
        super().__init__(self.message)


class RPCdisabled(Exception):
    def __init__(self, message="RPC control is disabled on the node"):
        self.message = message
        super().__init__(self.message)


class InvalidBalanceNumber(Exception):
    def __init__(self, message="Invalid balance number"):
        self.message = message
        super().__init__(self.message)


class EmptyResponse(Exception):
    def __init__(self, message="Empty server response"):
        self.message = message
        super().__init__(self.message)
