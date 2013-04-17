class AlkaneValidationError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


class AlkaneNotConnectedError(AlkaneValidationError):
    pass
class EmptyAlkaneError(AlkaneValidationError):
    pass
class CyclicAlkaneError(AlkaneValidationError):
    pass