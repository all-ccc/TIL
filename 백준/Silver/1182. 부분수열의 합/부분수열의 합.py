from itertools import combinations

N, S = map(int, input().split())    # N: 정수의 개수 / S: 부분수열의 합
n_lst = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):     # 1 ~ N개를 원소로 가지는 부분집합을 구하는 반복문
    for comb in combinations(n_lst, i):
        if sum(comb) == S:  # 부분수열의 합이 S가 되면
            cnt += 1        # cnt + 1 해줌
print(cnt)