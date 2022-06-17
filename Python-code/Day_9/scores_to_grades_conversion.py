student_scores={
  "harry":81,
  "Ron":78,
  "boom":99,
  "Bheem":100,
  "kaliya":40,
  "chutki":80,
}
# creating empty dictionary called student_grades
student_grades = {}
# writing code to add the grades in student_grades dictionary
for student in student_scores:
  score = student_scores[student]
  if score >90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds expetations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  elif  score > 50:
    student_grades[student] = "Good"
  else:
    student_grades[student]= "Fail"
print(student_grades)