student_score = input("Enter student marks/score\n").split()
for n in range(0,len(student_score)):
  student_score[n]= int(student_score[n])
  print(student_score)

max_score = 0
for max in student_score:
  if max > max_score:
    max_score = max
print(f"The heighest score in the class is:{max_score}")