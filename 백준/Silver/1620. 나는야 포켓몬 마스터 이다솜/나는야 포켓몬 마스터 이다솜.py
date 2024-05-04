import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pocket_dict = {}
for i in range(1, N+1):
    pocketmon = input().strip()     # 줄바꿈 문자 제거
    # 포켓몬 이름이 key인 경우와 포켓몬 번호가 key인 경우 둘 다 만들어줌
    pocket_dict[i] = pocketmon
    pocket_dict[pocketmon] = i


for _ in range(M):
    quiz = input().strip()
    if quiz.isdigit():      # 문제가 숫자라면
        print(pocket_dict[int(quiz)])
    else:                   # 문제가 문자라면
        print(pocket_dict[quiz])