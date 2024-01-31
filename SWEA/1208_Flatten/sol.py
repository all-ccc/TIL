import sys
# sys.stdin = open('input.txt')

for test in range(1, 11):
    dump = int(input())
    box_list = list(map(int, input().split()))
    # 덤프 횟수 만큼 반복
    for i in range(dump):
        max_box = max(box_list)
        min_box = min(box_list)

        # 최고점, 최저점의 박스가 있는 곳을 찾아서 덤프해줌
        box_list[box_list.index(max_box)] -= 1
        box_list[box_list.index(min_box)] += 1
        result = max(box_list) - min(box_list)

        # 이렇게 하면 안되는 이유
        # result = max_box - min_box -> 덤프해준 게 적용이 안된 채로 결과가 나옴
    
    print(f'#{test} {result}')



