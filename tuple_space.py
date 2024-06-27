space = []

def write(t):
    space.append(t)

def adjuste_tulpe(t, i):
    future_tuple = []
    for x in enumerate(t):
        if x[0] in i:
            future_tuple.append("*")
        else:
            future_tuple.append(x[1])
    return tuple(future_tuple)

def read(t):
    generic_item = []
    for x in enumerate(t):
        if x[1] == "*":
            generic_item.append(x[0])
    for s in space:
        if adjuste_tulpe(s, generic_item) == t:
            return s
        
def get(t):
    t2 = read(t)
    if t2 != None :
        space.remove(t2)
    return t2

write(("a","b","f","c",))
write(("a","b","d"))
write(("a","b","d","c",))
write(("a","b","x","c",))
write(("a","b","f","c",))
print(space)
print(get(("a", "b", "d", "*")))
print(get(("*", "b", "d", "*")))
print(space)