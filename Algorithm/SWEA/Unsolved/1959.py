# 1959 두 개의 숫자열

test_num = int(input()) # 10

sum = 0


for n in range(1, test_num + 1):

    max = 0
    a, b = map(int, input().split())
    if a < b:
        list_a = list(map(int, input().split()))
        list_b = list(map(int, input().split()))
        

    print('#%d %d' %(n, max))