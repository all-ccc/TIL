#  25314 코딩은 체육과목 입니다

a = int(input())

for i in range(a // 4):
    print('long', end =' ')
    if (i + 1) == (a // 4):
        print('int')
