#METHOD 1
total_sum = 0
for sum in range(1,101):
  if sum % 2 == 0:
    total_sum+=sum
print(f"The total sum of even numbers from 1 to 100 is {total_sum}")

#METHOD 2
total = 0
for sum in range(2,101,2):
  total += sum
print(total)
