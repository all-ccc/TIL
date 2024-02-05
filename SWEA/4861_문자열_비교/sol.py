import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{test} 1')
    else:
        print(f'#{test} 0')