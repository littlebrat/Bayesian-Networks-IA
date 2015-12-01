from Network.table import Table


class Variable:

    def __init__(self, values, alias=None, parents=None):
        self.__alias = alias
        self.__values = values
        self.__parents = parents
        self.__table = Table(values, parents)

    def parents(self):
        return self.__parents

    def values(self):
        return self.__values

    def alias(self):
        return self.__alias

    def set_table(self, var, values, parents):
        j = values[0]
        for l in range(1,len(values)):
            j = j * parents[l] + values[l]
        return j

    def __str__(self):
        return '[values: ' + str(self.__values) + '; alias: ' + str(self.__alias) + \
               '; parents:' + str(self.__parents) + ']'


