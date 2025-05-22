#total amount before tip
total = 100
#tip percentage
tip = 1.15
#amount of people
num_people = 2
#total with tip
total_with_tip = total * tip
#total tip split between 2
total_amount = total_with_tip / num_people
#how much pay
print(f" each person should pay ${total_amount:.2f}")

