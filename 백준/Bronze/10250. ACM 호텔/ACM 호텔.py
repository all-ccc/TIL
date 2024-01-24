import sys
# sys.stdin = open("input.txt", "r")

t_case = int(input())

for i in range(t_case):
    h, w, n = list(map(int, input().split()))
    breaker = False
    for y in range(1, w+1): # 1~12
        for x in range(1, h+1): # 1~6
            room_num = x * 100 + y
            n -= 1
            if n <= 0:
                breaker = True
                break
        if breaker == True:
                break
    print(room_num)