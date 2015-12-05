

class Query:

    def __init__(self):
        self.__wanted_variable = None
        self.__evidence = {}

    @staticmethod
    def from_file(path):
        qr = Query()
        with open(path) as file:
            for line in file:
                words = line.split()
                if len(words) == 2 and words[0] == 'QUERY':
                    qr.__wanted_variable = words[1].lower()
                elif len(words) > 1 and words[0] == 'EVIDENCE':
                    quantity = int(words[1])
                    if len(words) == 2 * quantity + 2:
                        for i in range(2, 2 * quantity + 1, 2):
                            qr.__evidence[words[i].lower()] = words[i+1].lower()
        return qr

    def wanted_variable(self):
        return self.__wanted_variable

    def evidence(self):
        return self.__evidence

    def query_check(self, network):
        """
        Code for this part is missing.
        """
        return True

    def __repr__(self):
        r = 'QUERY: \n'
        r += self.__wanted_variable +'\n'
        r += 'EVIDENCE: \n'
        for var in self.__evidence.keys():
            r += var + ': ' + self.__evidence[var] + '\n'
        return r[:-1]
