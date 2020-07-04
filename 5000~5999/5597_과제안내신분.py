student = []

for i in range(1,31,1):
    student.append(i)

for _ in range(28):
    s = int(input())
    student.remove(s)

for j in range(len(student)):
    print(student[j])
