import sys
# sys.stdin = open('input.txt')

T = int(input())
K = 9   # 정수의 최대값

for test in range(1, T+1):
    N = int(input())    # 리스트 길이
    data = list(map(int, input()))
    temp = [0] * N  # 정렬된 결과 저장
    counts = [0] * (K + 1)
    # 1. data에서 각 항목들의 발생 횟수 세고 -> counts 배열에 저장
    for num in data:
        counts[num] += 1

    # 2. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력
    max_count = 0
    max_num = 0
    for num, count in enumerate(counts):
        if count == max(counts):
            max_num = num
            max_count = count

    print(f'#{test} {max_num} {max_count}')



