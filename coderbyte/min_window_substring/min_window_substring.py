def MinWindowSubstring(strArr):
    d1 = dict()
    d2 = dict()
    for s in strArr[1]:
        if s in d1:
            d1.update({s: d1[s] + 1})
        else:
            d1[s] = 1
            d2.update({s: list()})

    start = len(strArr[0])
    end = -1

    for i, s in enumerate(strArr[0]):

        sum = 0
        for v in d1.values():
            sum += v
        if sum == 0:
            break

        if s in d1:
            if d1[s] <= 0:
                d2[s].pop(0)
            if d1[s] > 0:
                d1[s] -= 1
            d2[s].append(i)

    for v in d2.values():
        min_v = min(v)
        max_v = max(v)
        if min_v <= start:
            start = min_v
        if max_v >= end:
            end = max_v

    return strArr[0][start:end + 1]


# keep this function call here
print(MinWindowSubstring(["aaffhkksemckelloe", "fhea"]))
