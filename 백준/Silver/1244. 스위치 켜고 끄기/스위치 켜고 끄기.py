def on_off(i):
    if switch[i] == 0:
        switch[i] = 1
    else:
        switch[i] = 0


N = int(input())    # 스위치 개수
switch = [2] + list(map(int, input().split()))     # 스위치 상태(인덱스 값이랑 스위치 번호 맞추기 위해서 아무숫자나 앞에 넣음)
students = int(input())     # 학생 수
info = [list(map(int, input().split())) for _ in range(students)]   # 학생 성별(남1 여2), 받은 숫자


for gender, num in info:
    if gender == 1:     # 남자일 경우
        for i in range(num, N+1, num):  # 배수만 바꾸도록 step을 num으로
            on_off(i)

    else:               # 여자일 경우
        on_off(num)     # 일단 본인부터 바꿔주기
        left = num - 1
        right = num + 1
        while left >= 0 and right <= N and switch[left] == switch[right]:  # 인덱스 값 유효하면서 좌우대칭 값이 같은 최대 구간 찾기
            on_off(left)
            on_off(right)
            left -= 1
            right += 1

# 스위치 0번 인덱스는 출력할 필요 없으니까
for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()