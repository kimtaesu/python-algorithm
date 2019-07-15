N, M = map(int, input().split())

P = 1000
O = 1000
for n in range(M):
    PACKAGE, ONE = map(int, input().split())
    P = min(P, PACKAGE)
    O = min(O, ONE)

if P > 6 * O:
    P = 6 * O

if (N % 6) * O > P:
    print(int(N / 6) * P + P)
else:
    print(int(N / 6) * P + int(N % 6) * O)
