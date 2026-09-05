#logical operator
age = 25
citizen = True

print(age >= 18 and citizen == True )

age = 16 
citizen = True
print(age >= 18 and citizen == True) 

has_card = False
has_cash = True

print(has_card or has_cash)

is_logged_in = True

print(not is_logged_in)

#ATM eligibility checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#student sccholarship eligibility
marks = float(input("enter your marks :"))
attendence = float(input("enter attendence:"))

eligible = marks >= 85 and attendence >=75

print("scholarship Eligible:" , eligible)

#logical operator
