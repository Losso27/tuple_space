import sys
import time

from tuple_space import TupleSpace

MINIMUM_ARG_NUMBER = 4

def get_tuple(s):
    s = s.replace(")", "")
    s = s.replace("(", "")
    return tuple(x for x in s.split(","))

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

    while True:
        print("Digite [1] para blocking-get, [2] para read, [3] para write, [4] para get, [5] para imprimir o espaço e qualquer outra entrada para encerar:")
        string_input = input()
        string_input = string_input.strip()
        if string_input == "1":
            print("Operação [blocking-get] digite a tupla entre no formato (x,y,z):")
            i = input()
            t = get_tuple(i)
            print(tuple_space.blocking_get(t))
        elif string_input == "2":
            print("Operação [read] digite a tupla entre no formato (x,y,z):")
            i = input()
            t = get_tuple(i)
            print(tuple_space.read(t))
        elif string_input == "3":
            print("Operação [write] digite a tupla entre no formato (x,y,z):")
            i = input()
            t = get_tuple(i)
            tuple_space.write(t)
        elif string_input == "4":
            print("Operação [get] digite a tupla entre no formato (x,y,z):")
            i = input()
            t = get_tuple(i)
            print(tuple_space.get(t))
        elif string_input == "5":
            print(tuple_space.space)
        else:
            break


if __name__ == "__main__":
    main()
