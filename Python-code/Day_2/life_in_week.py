age = input ("what is your current age?\n")
age_as_int = int (age)
years_remaining = 90- age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, You have {weeks_remaining} weeks, You have {months_remaining} months")