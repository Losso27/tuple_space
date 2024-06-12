space = []

def write(t):
    space.append(t)

def adjuste_tulpe(t, i):
    future_tuple = []
    for x in enumerate(t):
        if x[0] in i:
            future_tuple.append(x[1])
    return tuple(future_tuple)

def read(t):
    itens = []
    for x in enumerate(t):
        if x[1] != "*":
            itens.append(x[0])
    t2 = adjuste_tulpe(t, itens)
    for s in space:
        if adjuste_tulpe(s, itens) == t2:
            return s
        
def get(t):
    t2 = read(t)
    space.remove(t2)

write(("a","b","f","c",))
write(("a","b","d","c",))
write(("a","b","d","c",))
print(space)
print(get(("a", "b", "d", "*")))
print(space)