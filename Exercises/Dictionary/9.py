n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name in students:
        students[name].append(grade)
    else:
        students[name] = [grade]

average_grades = {}
for name, grades in students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        average_grades[name] = average_grade

for name, average_grade in average_grades.items():
    print(f"{name} -> {average_grade:.2f}")
