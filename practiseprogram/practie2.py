
for i in range(int(input())):
    grade = int(input())
    if grade >= 38 and grade %5 >= 3:
        grade = (grade + 5) // 5 * 5
    print(grade)

