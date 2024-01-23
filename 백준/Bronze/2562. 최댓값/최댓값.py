import sys
# sys.stdin = open("input.txt", "r")

num_list = []

for _ in range(9):
    num_list.append(int(input()))

max_num = max(num_list)
max_index = num_list.index(max_num) + 1

print(max_num)
print(max_index)