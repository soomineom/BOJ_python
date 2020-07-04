train = []
people = 0

for _ in range(4):
    off, on = map(int, input().split())

    people += on
    people -= off

    train.append(people)
print(max(train))
