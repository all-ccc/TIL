import sys
sys.stdin = open('input.txt')

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = []       # pivot보다 작은 값
    right = []      # pivot보다 큰 값

    for num in lst[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quick_sort(left) + [pivot] + quick_sort(right)


T = int(input())
for test in range(1, T+1):
    n = int(input())
    unordered_lst = list(map(int, input().split()))
    result = quick_sort(unordered_lst)
    print(f'#{test} {result[n // 2]}')
