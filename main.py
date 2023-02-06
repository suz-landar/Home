tasks = 16
first_student = {1, 2, 3, 12, 13, 14, 5, 1}
second_student = {3, 4, 5, 14, 1, 7, 2, 9}
result = first_student | second_student
total = []
for i in range(1, tasks + 1):
    if i not in result:
        total.append(i)
print(len(total))