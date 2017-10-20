d1 = {'s': 'LG', 'i': 7, 'd': 4.3}
d2 = {'s': 4, 'i': 4, 'd': '2017'}

print ({k: type(d1[k])(d2[k]) for k in d2})
# print ({k : type(d1[k])(v) for (k,v) in d2})
# ValueError: need more than 1 value to unpack
print ({k: type(d1[k])(v) for (k, v) in d2.items()})
print ([type(d1[k])(v) for (k, v) in d2.items()])

g = {'A': set(['B', 'D']),
     'B': set(['A', 'C', 'D']),
     'C': set(['B', 'D']),
     'D': set(['A', 'B', 'C'])}


def test(g, x, y, p=None):
    if p is None:
        p = [x]
    if x == y:
        yield p
    for i in g[x] - set(p):
        yield from test(g, i, y, p + [i])


print(len(list(test(g, 'A', 'D'))),)
print(len(list(test(g, 'C', 'B'))),)
