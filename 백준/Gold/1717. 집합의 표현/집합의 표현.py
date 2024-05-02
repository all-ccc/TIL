import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    else:
        if find(a) == find(b):  # 부모가 같으면 (= 같은 집합에 포함)
            print('YES')
        else:
            print('NO')

