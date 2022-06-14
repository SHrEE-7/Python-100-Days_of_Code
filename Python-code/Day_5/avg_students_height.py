student_heights = input("Enter student heights\n").split()
for n in range(0,len(student_heights)):
  student_heights[n]=int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
print(total_height)

num_of_student = 0
for student in student_heights:
  num_of_student += 1
avg_of_heights = round(total_height / num_of_student)
print(avg_of_heights)