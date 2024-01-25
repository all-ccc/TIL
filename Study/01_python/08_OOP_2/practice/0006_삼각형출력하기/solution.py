import sys
sys.stdin = open('input.txt')

n = int(input())
# range는 0부터 n-1까지지만, 별은 1개부터 n개까지 필요하므로...

# for i in range(1, n+1):
#     for j in range(i):
#         print('*', end='')
#     print()

for i in range(1, n+1):
    print('*' * i)