from datetime import date
dob = date(1993,3,20)

today = date.today()

age = abs(today-dob)
print("your age",int(age.days/365))
