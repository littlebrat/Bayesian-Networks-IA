from Network.network import Network


class Problem:
    """
        This class defines a query problem given the network BN, the query variable and the evidence.
    """

    @staticmethod
    def ve_inference(bayesnet, query, ordering):
        # The variable that we want to know.
        distribution = query.wanted_variable()
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
            new_factor.sum_on_var(var)
            # Add factor to the remaining tables.
            factors.append(new_factor)
            #### NORMALIZATION IS MISSING
        return factors

