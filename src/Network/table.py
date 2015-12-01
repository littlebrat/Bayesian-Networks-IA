from numpy import ndarray


class Table:

    def __init__(self, values, other_vars):
        if other_vars is not None:
            self.__table = ndarray((len(values),len(other_vars)),float)
        else:
            self.__table = ndarray((len(values),0),float)

