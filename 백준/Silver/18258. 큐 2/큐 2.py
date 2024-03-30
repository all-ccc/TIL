import sys
from collections import deque
# list로 했다가 시간초과 떠서 deque 사용

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':   # push 명령이라면 (출력 필요 X)
        q.append(command[1])    # 숫자를 append 해준다 ~

    elif command[0] == 'pop':
        if q:
            print(q.popleft())
        else:   # q에 들어있는 정수가 없는 경우
            print(-1)

    elif command[0] == 'size':
        print(len(q))

    elif command[0] == 'empty':
        if q:   # q가 비어있지 않다면
            print(0)
        else:   # q가 비어있으면
            print(1)

    elif command[0] == 'front':
        if q:   # q가 비어있지 않다면
            print(q[0])     # q의 가장 앞에 있는 정수 출력
        else:   # q가 비어있으면
            print(-1)

    else:   # back
        if q:  # q가 비어있지 않다면
            print(q[-1])  # q의 가장 뒤에 있는 정수 출력
        else:  # q가 비어있으면
            print(-1)