import sys
sys.stdin = open('input.txt')

for test in range(1, 11):
    length = int(input())   # 회문의 길이
    data = [list(map(int, input().split())) for _ in range(8)]
    for x in range(8 - length):
        for y in range(8 - length):
            pass
