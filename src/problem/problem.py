

class Problem:
    """
        This class defines a query problem given the network BN, the query variable and the evidence.
    """

    def __init__(self, bayesnet, query, evidence):
        self.bn = bayesnet
        self.query_set = query
        self.evidence_set = evidence