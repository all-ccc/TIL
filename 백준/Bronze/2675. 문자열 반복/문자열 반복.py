import sys
# sys.stdin = open("input.txt", "r")

case_num = int(input())

for _ in range(case_num):
    num, string = input().split()
    for str in string:
        print(str * int(num), end='')
    print()