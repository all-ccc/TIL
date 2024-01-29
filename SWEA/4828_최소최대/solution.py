import sys
# sys.stdin = open('sample_input.txt')

test_num = int(input())

for test in range(test_num):
    numbers = int(input())
    num_list = list(map(int, input().split()))

    min_num = min(num_list)
    max_num = max(num_list)
    result = max_num - min_num
    print(f'#{test+1} {result}')

