

class Problem:
    """
        This class defines a query problem given the network BN, the query variable and the evidence.
    """

    @staticmethod
    def ve_inference(bayesnet, query, evidence, ordering):

        return 0