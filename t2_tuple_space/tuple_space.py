from pysyncobj import SyncObj, replicated


class TupleSpace(SyncObj):
    def __init__(self, self_node_address, partners_node_addresses):
        super(TupleSpace, self).__init__(self_node_address, partners_node_addresses)
        self.__counter = 0
        print("self:", self_node_address)
        print("partners:", partners_node_addresses)

    @replicated
    def incCounter(self):
        self.__counter += 1

    def getCounter(self):
        return self.__counter
