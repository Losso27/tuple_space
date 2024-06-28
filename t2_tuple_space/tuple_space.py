from pysyncobj import SyncObj, SyncObjConf, replicated


class TupleSpace(SyncObj):
    def __init__(self, self_node_address, partners_node_addresses):
        cfg = SyncObjConf(dynamicMembershipChange = True)
        super(TupleSpace, self).__init__(self_node_address, partners_node_addresses, cfg)
        self.space = []
        print("self:", self_node_address)
        print("partners:", partners_node_addresses)

    def adjust_tuple(self, t, i):
        future_tuple = []
        for x in enumerate(t):
            if x[0] in i:
                future_tuple.append("*")
            else:
                future_tuple.append(x[1])
        return tuple(future_tuple)


    def read(self, t):
        generic_item = []
        for x in enumerate(t):
            if x[1] == "*":
                generic_item.append(x[0])
        for s in self.space:
            if self.adjust_tuple(s, generic_item) == t:
                return s

    @replicated
    def write(self, t):
        self.space.append(t)
        
    @replicated
    def remove(self, t):
        self.space.remove(t)

    @replicated
    def get(self, t):
        t2 = self.read(t)
        if t2 != None:
            self.space.remove(t2)
            return t2
