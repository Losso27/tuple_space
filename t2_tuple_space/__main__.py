import sys
import time

from tuple_space import TupleSpace

MINIMUM_ARG_NUMBER = 4


def main():
    if len(sys.argv) < MINIMUM_ARG_NUMBER:
        print("Usage: %s self_port partner1_port partner2_port ..." % sys.argv[0])
        sys.exit(-1)

    port = sys.argv[1]
    partners = sys.argv[2:]

    tuple_space = TupleSpace(
        "localhost:%s" % port,
        list(map(lambda partnet_port: "localhost:%s" % partnet_port, partners)),
    )

    n = 0
    while True:
        print("Digite [1] para get, [2] para read, [3] para write, [4] para imprimir o espaço e qualquer outra entrada para encerar:")
        string_input = input()
        string_input = string_input.strip()
        if string_input == "1":
            print("digite a tupla entre no formato (x,y,z):")
            a = input()
            a = a.replace(")", "")
            a = a.replace("(", "")
            a = tuple(x for x in a.split(","))
            print(tuple_space.get(a))
        elif string_input == "2":
            print("digite a tupla entre no formato (x,y,z):")
            a = input()
            a = a.replace(")", "")
            a = a.replace("(", "")
            a = tuple(x for x in a.split(","))
            print(tuple_space.read(a))
        elif string_input == "3":
            print("digite a tupla entre no formato (x,y,z):")
            a = input()
            a = a.replace(")", "")
            a = a.replace("(", "")
            a = tuple(x for x in a.split(","))
            tuple_space.write(a)
        elif string_input == "4":
            print(tuple_space.space)
        else:
            break


if __name__ == "__main__":
    main()
