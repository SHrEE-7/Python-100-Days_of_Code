print("welcome to tip calculator\n")
bill_amount = float(input("what was the total bill amount?\n"))
tip = int (input("what percentage tip you would like to give?\n10, 12 or 15\n"))
people = int(input("how many peoplet to split the bill?\n"))
tip_as_percentage = tip /100
total_tip_amount = bill_amount * tip_as_percentage
total_bill_amount = bill_amount + total_tip_amount
bill_per_person = total_bill_amount / people
final_amount = round(bill_per_person,2)
print(f"You have to pay ₹{final_amount}")