N, M = 4, 3
knows = [1]

parties = [
    [2, 1, 2],
    [1, 3],
    [3, 2, 3, 4]
]


def scc(k):
    for p in parties:
        print(p[1:])

for k in knows:
    scc(k)
