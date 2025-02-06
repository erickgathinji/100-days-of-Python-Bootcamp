print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int (input("How many people to split the bill? "))
new_bill_with_tip = (1 + tip/100) * bill
# round to 2 dp
everyone_to_pay = "{:.2f}".format(new_bill_with_tip / people)
print(f"Each person should pay: ${everyone_to_pay}")
