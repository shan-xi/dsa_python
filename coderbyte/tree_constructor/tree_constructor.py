def TreeConstructor(strArr):
    t = list()
    for s in strArr:
        n1 = s[s.index('(') + 1:s.index(',')]
        n2 = s[s.index(',') + 1:s.index(')')]
        t.append((n1, n2))

    p = dict()
    np = dict()
    for s in t:
        n1 = int(s[0])
        n2 = int(s[1])

        if n1 not in np:
            np.update({n1: set()})
        np[n1].add(n2)
        if len(np[n1]) > 1:
            return False

        if n2 not in p:
            p.update({n2: set()})
        p[n2].add(n1)
        if len(p[n2]) > 2:
            return False

    return True

# keep this function call here
# print(TreeConstructor(input()))
