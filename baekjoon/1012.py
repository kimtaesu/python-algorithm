import sys

def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if a[nx][ny] and not check[nx][ny]:
            dfs(nx, ny)


def solve():
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] and not check[i][j]:
                dfs(i, j)
                ans += 1
    print(ans)


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    check = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        a[y][x] = 1
    solve()
