import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    N = int(input())

    num_list = [list(map(int, input().split())) for _ in range(100)]
    # 100X100 크기의 2차원 배열 만들기

    row_list = [] # 행의 합 넣을 배열
    col_list = [] # 열의 합 넣을 배열
    dia_list = [] # 대각선의 합 넣을 배열

    # 행의 합 구하는 반복문
    for i in range(100):
        sum_result = sum(num_list[i])
        row_list.append(sum_result)
    row_max = max(row_list) # 행의 합 중 최대

    # 열의 합 구하는 반복문
    for x in range(100):
        col_sum = 0
        for y in range(100):
            col_sum += num_list[y][x]
            col_list.append(col_sum)
    col_max = max(col_list) # 열의 합 중 최대

    # 대각선의 합 구하는 반복문 1
    dia_sum_R = 0
    dia_sum_L = 0
    for i in range(100):
        dia_sum_R += num_list[i][i]
        dia_sum_L += num_list[99-i][i]
        dia_list.append(dia_sum_R)
        dia_list.append(dia_sum_L)

    dia_max = max(dia_list)  # 대각선의 합 중 최대

    max_sum = max(row_max, col_max, dia_max)
    print(f'#{test} {max_sum}')


