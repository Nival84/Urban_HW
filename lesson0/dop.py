grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_student = list(students)
list_student.sort()
a1 = sum(grades[0])/len(grades[0])
a2 = sum(grades[1])/len(grades[1])
a3 = sum(grades[2])/len(grades[2])
a4 = sum(grades[3])/len(grades[3])
a5 = sum(grades[4])/len(grades[4])
V1 = {list_student[0]: a1, list_student[1]: a2, list_student[2]: a3, list_student[3]: a4, list_student[4]: a5}
print(V1)