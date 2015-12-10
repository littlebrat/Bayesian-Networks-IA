import sys
from problem.query import Query
from problem.problem import Problem
from Network.network import Network


def main(args):

    verbose = False

    if len(args) == 3 or len(args) == 4:

        if len(args) == 4 and args[3] == '-verbose':
            verbose = True

        bayes_name = None
        bayes_net = None

        if args[1][-3:] == '.bn':
            bayes_name = args[1][:-3]
            bayes_net = Network.from_file(args[1])
        else:
            return Exception('Expected .bn file.')

        query_name = None
        query = None

        if args[2][-3:] == '.in':
            query_name = args[2][:-3]
            query = Query.from_file(args[2])
        else:
            return Exception('Expected .in file.')

        if bayes_name is not None and query_name is not None:

            # Do the inference
            result, log = Problem.ve_inference(bayes_net, query, Problem.random_order(bayes_net, query))

            # Check if log mode is on
            if verbose:
                Problem.to_file(query_name, result, query, log)
            else:
                Problem.to_file(query_name, result, query)
    return 0


if __name__ == "__main__":
    main(sys.argv)
