# 백준 3052

num_list = []

for i in range(10):
    x = int(input())
    num_list.append(x % 42)

print(len(set(num_list)))