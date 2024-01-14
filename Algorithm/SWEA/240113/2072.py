a = int(input())

for i in range(a):
    numbers = list(map(int, input().split()))
    sum = 0

    for num in range(len(numbers)):
        if numbers[num] % 2 == 1:
            sum += numbers[num]
            
    print('#%d' % (i+1), sum)
