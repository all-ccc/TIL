# 2068 최대수 구하기

a = int(input())

for i in range(a):
    print('#%d' % (i+1), max(list(map(int, input().split()))))
    