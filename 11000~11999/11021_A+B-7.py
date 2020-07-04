t = int(input())
res = []

for i in range(t):
    a,b = map(int, input().split())
    c = a+b
    res.append(c)


for i in range(len(res)):
    print("Case #{}: {}".format(i+1,res[i]))
