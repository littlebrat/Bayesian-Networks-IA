import sys
from problem.query import Query


qr = Query.from_file('test_files/enunciado.in')

print(qr)


def main(args):
    return 0


if __name__ == "__main__":
    main(sys.argv)
