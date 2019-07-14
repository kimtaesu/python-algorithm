def wrap(dist):
    n = 1

    while (True):
        powN = n * n
        minN = powN - n + 1
        maxN = powN + n

        if minN <= dist <= maxN:
            if minN <= dist <= powN:
                wrapCnt = (n << 1) - 1
            else:
                wrapCnt = n << 1
            break
        n += 1
    return wrapCnt


print(wrap(3))
