#reverse engineering

print("➗ Welcome to the tip calculator ➗")

# bill_amount= print(type(input("What was the total bill? $"))) # In order to be able to do maths, we have to change this into a number format (float or integer).
bill_amount= float(input("What was the total bill? $"))
tip_amount = int(input("What percentage tip would you like to give? 10 12 15 20 "))
people_split = int(input("How many people to split the bill? "))
tip_as_percent = tip_amount / 100
total_tip_amount = bill_amount * tip_as_percent
total_bill = bill_amount + total_tip_amount
total_per_person = round(total_bill / people_split, 2)
#final_amount = round(total_per_person, 2)


# bill_with_tip = tip_amount / 100 * bill_amount + bill_amount
print(f"The total bill with tip is {total_bill} ")
print(f"The bill split in {people_split} will be: {total_per_person} per person.")

#print(bill_amount * tip_amount / people_split)
