from Network.network import Network
from random import shuffle


class Problem:
    """
        This class defines a query problem given the network BN, the query variable and the evidence.
    """

    @staticmethod
    def ve_inference(bayesnet, query, ordering):
        # Evidence we got from the file.
        evidence = query.evidence()
        # Get all the tables in the network.
        factors = bayesnet.get_factors()
        # Check consistency with the evidence.
        for f in factors:
            f.evidence_eliminate(evidence)
        # Main part of the algorithm.
        for var in ordering:
            # Get factors with 'var' in them.
            factors_with_var = []
            factors_in = []
            for f in factors:
                if f.has_variable(var):
                    factors_with_var.append(f)
                else:
                    factors_in.append(f)
            factors = factors_in
            # Multiply all the factors with 'var' in them.
            new_factor = factors_with_var.pop()
            while factors_with_var:
                aux = factors_with_var.pop()
                new_factor = new_factor.multiply_tables(aux)
            # Sum on the current 'var'.
            new_factor_aux = new_factor.sum_on_var(var)
            # Add factor to the remaining tables.
            factors.append(new_factor_aux)
        # Last step, multiply the remaining factors.
        new_factor = factors.pop()
        while factors:
            aux = factors.pop()
            new_factor = new_factor.multiply_tables(aux)
        # Normalization
        new_factor.normalize()
        return new_factor, None

    @staticmethod
    def random_order(bayesnet, query):
        # The variable that we want to know.
        wanted = [query.wanted_variable()]
        # Evidence we got from the file.
        evidence = set(query.evidence())
        # Get all the variables in the bayesian network
        all_variables = set(bayesnet.vars())
        order = all_variables.difference(wanted)
        order = list(order.difference(evidence))
        shuffle(order)
        return order

    @staticmethod
    def to_file(filename, result, query, log=None):
        # Method that outputs the solution in cnf file.
        with open(filename + '.sol', "w") as file:
            res = '########## SOLUTION ########## \n'
            wanted = query.wanted_variable()
            res += 'QUERY ' + wanted +'\n'
            all_evidences = query.evidence()
            res += 'EVIDENCE '
            for evidence in all_evidences.keys():
                res += evidence + ' ' + all_evidences[evidence] + ' '
            res += '\n' + 'QUERY_DIST '
            final_events = result.all_events()
            for event in final_events:
                res += event.get_value(wanted) + ' ' + str(round(event.probability(), 3)) + ' '
            file.write(res)