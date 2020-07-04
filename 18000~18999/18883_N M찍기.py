n,m = map(int, input().split())
one = 1

for i in range(n):
    for k in range(m):
        if(k == m-1): #행의 마지막 숫자일때
            print(one)
            one += 1
        else:
            print(one, end=' ')
            one += 1
