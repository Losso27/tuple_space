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
        if n == 20:
            break
        time.sleep(0.5)

        tuple_space.incCounter()
        print(tuple_space.getCounter())
        n += 1


if __name__ == "__main__":
    main()
