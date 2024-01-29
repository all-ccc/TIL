import sys
# sys.stdin = open('input.txt')

for test in range(10):
    buildings = int(input())
    height_list = list(map(int, input().split()))
    view_building = 0
    for i in range(2, buildings - 1):
        left_right = []
        # append 하면 2차열 배열이 생김
        left_right.extend(height_list[i-2:i])
        left_right.extend(height_list[i+1:i+3])
        max_height = max(left_right)
        if height_list[i] > max_height:
            view_building += (height_list[i] - max_height)
    print(f'#{test+1} {view_building}')



