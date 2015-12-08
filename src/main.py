import sys
from problem.query import Query
from problem.problem import Problem
from Network.network import Network


qr = Query.from_file('test_files/enunciado.in')

print(qr)

print()

net = Network.from_file('test_files/enunciado.bn')

print(net)

res = Problem.ve_inference(net, qr, Problem.random_order(net, qr))

print(res)

def main(args):
    return 0


if __name__ == "__main__":
    main(sys.argv)
