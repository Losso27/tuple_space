from pysyncobj import SyncObj, replicated


class TupleSpace(SyncObj):
    def __init__(self, self_node_address, partners_node_addresses):
        super(TupleSpace, self).__init__(self_node_address, partners_node_addresses)
        self.space = []
        print("self:", self_node_address)
        print("partners:", partners_node_addresses)

    def adjust_tuple(self, t, i):
        future_tuple = []
        for x in enumerate(t):
            if x[0] in i:
                future_tuple.append(x[1])
        return tuple(future_tuple)

    def read(self, t):
        itens = []
        for x in enumerate(t):
            if x[1] != "*":
                itens.append(x[0])
        t2 = self.adjust_tuple(t, itens)
        for s in self.space:
            if self.adjust_tuple(s, itens) == t2:
                return s

    @replicated
    def write(self, t):
        self.space.append(t)

    @replicated
    def get(self, t):
        t2 = self.read(t)
        if t2 is not None:
            self.space.remove(t2)
