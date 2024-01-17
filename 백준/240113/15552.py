# 15552 빠른 A+B

import sys
#  import sys 코드는 sys를 포함하겠다는 것으로
# sys.stdin.readline()을 사용할 수 있도록 하는 코드

num = int(input())
for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
