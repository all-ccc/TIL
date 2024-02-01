import sys
sys.stdin = open('input.txt')


def binary_search(arr, N, key):
    # arr = 검색을 할 배열
    # N = 배열의 길이
    # key = 찾을 값

    start = 0   # 배열의 첫 인덱스 값
    end = N - 1  # 배열의 마지막 인덱스 값 (399)
    cnt = 0  # 탐색을 몇 번 했는지 세는 cnt 변수

    while start <= end:
        cnt += 1
        middle = (start + end) // 2  # 199
        if arr[middle] == key:  # 검색 성공
            break
        elif arr[middle] > key:   # 중앙값이 키보다 크면
            end = middle
        else:   # 중앙값이 키보다 작으면
            start = middle
    return cnt


T = int(input())
for test in range(1, T+1):
    P, A, B = map(int, input().split())
    # P : 전체 페이지 수
    # A : A가 찾아야 할 페이지
    # B : B가 찾아야 할 페이지
    page = [i for i in range(1, P+1)]   # 교과서의 페이지를 배열로

    A_cnt = binary_search(page, P, A)   # A의 탐색 수
    B_cnt = binary_search(page, P, B)   # B의 탐색 수

    if A_cnt < B_cnt:
        print(f'#{test} A')
    elif A_cnt > B_cnt:
        print(f'#{test} B')
    else:
        print(f'#{test} 0')

