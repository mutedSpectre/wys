class Equality:
    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            self.__dict__ == other.__dict__
    