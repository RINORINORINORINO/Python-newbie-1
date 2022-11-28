number = 0
for i in [90, 65, 77, 53, 20]:
    number = number + 1
    if i > 60: continue
    print("%d번 학생 합격입니다!" % number)

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end = "")
    print('')