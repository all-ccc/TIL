import sys
sys.stdin = open('input.txt')

def merge_sort(unsorted_list):  # 분할 과정
    # 크기가 1이하면 바로 반환
    if len(unsorted_list) <= 1:
        return unsorted_list

    # 리스트를 2분할
    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    # 2분할한 리스트를 각각 merge sort진행
    left_ = merge_sort(left)
    right_ = merge_sort(right)

    return merge(left_, right_)


def merge(left, right):     # 병합 과정
    global cnt
    i, j = 0, 0
    sorted_list = []

    if left[-1] > right[-1]:    # 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
        cnt += 1

    # left와 right에 서로 비교할 값이 남아 있을 때까지
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])     # 작은 것부터 append
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):    # left_lst만 남아있는 경우
        sorted_list.append(left[i])
        i += 1

    while j < len(right):   # right_lst만 남아있는 경우
        sorted_list.append(right[j])
        j += 1

    return sorted_list

# 최소 단위가 될 때까지 균등한 크기로 분할 -> 부분 리스트들을 정렬하면서 병합
T = int(input())
for test in range(1, T+1):
    N = int(input())
    unsorted_list = [int(x) for x in input().split()]
    cnt = 0
    result = merge_sort(unsorted_list)
    print(f'#{test} {result[N//2]} {cnt}')