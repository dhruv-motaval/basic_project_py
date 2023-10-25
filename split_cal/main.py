print("Welcome to the tip calculator!")

bill_amount = float(input("What was the total bill?"))

tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

persons=int(input("How many people to split the bill?"))


tip_amount = bill_amount * (tip_percentage/100)

total_bill = bill_amount+ tip_amount

split = total_bill / persons

share_of_people = bill_amount/persons

shere_of_tip = tip_amount/persons

print(f"Each person should pay: ${round(split,2)}")
