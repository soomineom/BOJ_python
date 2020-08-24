from collections import deque
import sys
input = sys.stdin.readline

q = deque()

n = int(input())
for _ in range(n):
    com = input().split()

    if com[0] == 'push':
        q.append(int(com[1]))
    elif com[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif com[0] == 'size':
        print(len(q))
    elif com[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif com[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif com[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[len(q)-1])
