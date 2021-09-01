def add_link(e, a, b):
    aux = {a, b}
    for v in e[::-1]:
        print('v->',v, e)
        if a in v or b in v:
            e.remove(v)
            aux.update(v)
    e.append(aux)
    return e


def findPair(e, a, b):
    for v in e:
        if (a in v) != (b in v):
            return True
    return False


nt, nm, nd = map(int, input().split())
em, ed = [], []

for _ in range(nm):
    a, b = map(int, input().split())
    em = add_link(em, a, b)

for _ in range(nd):
    a, b = map(int, input().split())
    ed = add_link(ed, a, b)

print(em)
print(ed)
print('- '*25)
for i in range(1, nt+1):
    for j in range(i+1, nt+1):
        if i != j:
            pm = findPair(em, i, j)
            pd = findPair(ed, i, j)
            if pm and pd:
                print('-->',i,j)
                em = add_link(em, i, j)
                ed = add_link(ed, i, j)
                print(em)
                print(ed)
