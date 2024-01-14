# 1959 두 개의 숫자열

test_num = int(input())

sum = 0

max = 0

for n in range(1, test_num+1):

    a, b = map(int, input().split())


    print('#%d %d' %(n, max))