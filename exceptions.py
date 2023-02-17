class HeatingInterrupt(Exception):
    def __init__(self, message="Heating interrupt"):
        super().__init__(message)