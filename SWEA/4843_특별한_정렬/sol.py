import sys
sys.stdin = open('input.txt')


# # 선택정렬 안 쓰는 방법. 근데 선택정렬 써야...
# def special_sort(arr, N):
#     new_arr = []
#     while len(new_arr) < 10:
#         mm_arr = [max(arr), min(arr)]    # 현재 arr에서 최댓값과 최솟값 한 쌍
#         new_arr.extend(mm_arr)
#         arr.remove(min(arr))
#         arr.remove(max(arr))
#     return new_arr

def selection_sort(arr, N):
    for i in range(N-1):
        idx = i # 구간의 최솟값 위치
        if i % 2 == 0:  # 최댓값 들어와야 하는 짝수 인덱스일 경우
            for j in range(i + 1, N):  # 실제 최댓값을 찾을 위치 j
                if arr[j] > arr[idx]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]  # 최댓값을 구간의 맨 앞으로 이동([0] <-> [1])
        else:   # 최솟값 들어와야 하는 홀수 인덱스일 경우
            for j in range(i + 1, N):
                if arr[j] < arr[idx]:
                    idx = j
            arr[i], arr[idx] = arr[idx], arr[i]  # 최솟값을 구간의 맨 앞으로 이동([0] <-> [1])
    return arr


T = int(input())
for test in range(1, T+1):
    N = int(input())    # N : 정수의 개수
    n_list = list(map(int, input().split()))
    result = selection_sort(n_list, N)
    # result = special_sort(n_list, N)

    print(f'#{test}', *result[0:10])
