from Network.variable import Variable


class Network:

    def __init__(self):
        self.__nodes = {}

    @staticmethod
    def from_file(path):
        """
        This method reads .bn file that represents a Bayesian Network.
        :param path: File path.
        :return: a Network object.
        """
        net = Network()
        # this method loads a file into a object of this class.
        with open(path) as file:
            if path[-3:] is '.bn':
                while True:
                    # Reads the line and splits the line in an array of words
                    line = file.readline()
                    words = line.split()
                    # Verify if we are in a case of a VAR description or a CPT description.
                    if words[0] is 'VAR':
                        no_endline = True
                        name = None
                        alias = None
                        parents = []
                        values = []
                        while no_endline:
                            line = file.readline()
                            words = line.split()
                            if words[0] is 'name':
                                name = words[1]
                            elif words[0] is 'alias':
                                alias = words[1]
                            elif words[0] is 'parents':
                                parents = words[1:len(words)]
                            elif words[0] is 'values':
                                values = words[1:len(words)]
                            else:
                                no_endline = False
                        net.add_var(name, alias, parents, values)
                    elif words[0] is 'CPT':
                        no_endline = True
                        var = None

                        while no_endline:
                            line = file.readline()
                            words = line.split()
                            if words[0] is 'var':
                                var = words[1]
                                var = net.real_name(var)

                    elif words[0] is '#':
                        continue
            else:
                return Exception('File has not the appropriate extension.')
        return net

    def add_var(self, name, values, parents=None, alias=None):
        """
        Adds variable to the network.
        :param name: real name of the discrete variable.
        :param values: possible values this variable can take.
        :param parents:
        :param alias:
        :return: void
        """
        self.__nodes[name] = Variable(values, parents, alias)

    def real_name(self, name):
        """
        This method converts an alias to the real name of the variable.
        If it is already the real name of the variable it returns name.
        :param name: The name or alias of the variable
        :return: The name of the variable
        """
        if name in self.__nodes.keys():
            return name
        else:
            for k in self.__nodes.keys():
                if name is self.__nodes[k].alias:
                    return k
        return None

    def get_factors(self):
        return 0

    def __repr__(self):
        r = '['
        for var in self.__nodes.keys():
            r += 'var: ' + var + ' = ' + str(self.__nodes[var]) + '; '
        return r + ']'