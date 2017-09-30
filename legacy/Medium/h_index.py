def hIndex(citations) :
    citations.sort()
    h_max = 0
    flag = False
    if len(citations) == 1:
        return citations[0]

    if len(citations) == 0:
        return []

    for i in range(len(citations)):
        h = len(citations) - citations[i]

        if (len(citations[:i]) == h):
            flag = True
            res = h

        if flag is True:
            if h_max <= res:
                h_max = res
    print citations[h_max]

hIndex([3, 0, 6, 1, 5])
hIndex([])
hIndex([0,1])
