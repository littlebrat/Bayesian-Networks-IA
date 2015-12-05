from Network.variable import Variable
from Network.table import Table
from Network.event import Event

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
            line = file.readline()
            while line != '':
                # Reads the line and splits the line in an array of words
                words = line.split()
                # Verify if we are in a case of a VAR description or a CPT description.
                if len(words) > 0:
                    if words[0] == 'VAR':
                        name = None
                        alias = None
                        parents = []
                        values = []
                        line = file.readline()
                        while line != '\n':
                            words = line.split()
                            if words[0] == 'name':
                                name = words[1].lower()
                            elif words[0] == 'alias':
                                alias = words[1].lower()
                            elif words[0] == 'parents':
                                parents = [w.lower() for w in words[1:len(words)]]
                            elif words[0] == 'values':
                                values = [w.lower() for w in words[1:len(words)]]
                            line = file.readline()
                        net.add_var(name, values, parents, alias)
                    elif words[0] == 'CPT':
                        line = file.readline()
                        vars_table = []
                        aux_table = None
                        while line != '\n' and line != '':
                            words = line.split()
                            if words[0] == 'var':
                                var = net.real_name(words[1].lower())
                                vars_table.append(var)
                                parents = net.__nodes[var].parents()
                                for i in range(len(parents)):
                                    vars_table.append(net.real_name(parents[i]))
                                aux_table = Table(vars_table)
                                line = file.readline()
                            elif words[0] == 'table':
                                if len(words) > 1 and (len(words) - 1) % (len(vars_table) + 1) == 0:
                                    for i in range(1, len(words), len(vars_table) + 1):
                                        event = {}
                                        for j in range(0, len(vars_table)):
                                            event[vars_table[j]] = words[i + j]
                                        prob = float(words[i + len(vars_table)])
                                        aux_table.add_event(Event(event, prob))
                                line = file.readline()
                                while line != '\n' and line != '':
                                    words = line.split()
                                    event = {}
                                    for i in range(len(words) - 1):
                                        event[vars_table[i]] = words[i].lower()
                                    prob = float(words[-1])
                                    aux_table.add_event(Event(event, prob))
                                    line = file.readline()
                            var = net.var(vars_table[0])
                            var.set_table(aux_table)
                line = file.readline()
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
        self.__nodes[name] = Variable(values, alias, parents)

    def var(self, name):
        return self.__nodes[name]

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
                if name == self.__nodes[k].alias():
                    return k
        return None

    def get_factors(self):
        res = []
        for key in self.__nodes.keys():
            res.append(Table.deepcopy(self.__nodes[key].table()))
        return res

    def __repr__(self):
        r = ''
        for var in self.__nodes.keys():
            r += 'var: ' + var + '\n' + str(self.__nodes[var]) + '\n \n'
        return r