import sys
# sys.stdin = open('sample_input.txt')

test_case = int(input())

for test in range(1, test_case + 1):
    n, section = map(int, input().split())
    num_list = list(map(int, input().split()))
    sum_list = []
    for sum_case in range(n - section + 1):
        result = 0
        for i in range(sum_case, sum_case + section):
            result += num_list[i]
        sum_list.append(result)
    print(f'#{test}', (max(sum_list) - min(sum_list)))


