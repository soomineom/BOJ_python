n = int(input())

for i in range(n):
    s = list(input())
    s[0] = s[0].upper()
    print("".join(s))
