import sys
from problem.query import Query
from Network.network import Network


qr = Query.from_file('test_files/enunciado.in')

print(qr)

net = Network.from_file('test_files/enunciado.bn')




def main(args):
    return 0


if __name__ == "__main__":
    main(sys.argv)
