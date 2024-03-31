from collections import defaultdict

N = int(input())    # 사진 개수
rec = int(input())  # 추천 횟수
st_num = list(map(int, input().split()))
st_dict = defaultdict(int)  # 딕셔너리에 키값이 없을 경우 그 문자를 키로 등록하고 값은 0으로 초기화
result = []
for num in st_num:
    st_dict[num] += 1         # 추천횟수(value) 1 증가
    if num in result:     # 이미 result에 있는 학생이라면 넘어가
        continue

    elif len(result) < N:   # result에 들어갈 자리가 남았다면
        result.append(num)

    else:   # result가 다 찼을 경우
        min_rec = 1000
        for i in result:    # 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제
            if st_dict[i] < min_rec:
                min_rec = st_dict[i]
                min_stu = i     # 추천 횟수 가장 적은 학생 갱신
        result.remove(min_stu)
        st_dict[min_stu] = 0    # 삭제된 학생의 추천 횟수는 다시 0으로..
        result.append(num)
result.sort()
print(*result)