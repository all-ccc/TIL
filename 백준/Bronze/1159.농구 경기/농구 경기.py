import sys
# sys.stdin = open("input.txt", "r")

n = int(input())
name_list = []


for i in range(n):
    last_name = input()[0]
    name_list.append(last_name)

name_set = set(name_list)
player_list = []

for i in range(len(name_set)):
    n = name_list.count(list(name_set)[i])
    if n >= 5:
        player_list.append(list(name_set)[i])
player_list.sort()
if len(player_list) > 0:
    for player in player_list:
        print(player, end='')
else:
    print('PREDAJA')