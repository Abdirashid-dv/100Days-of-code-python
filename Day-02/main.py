from art import logo

print(logo)

#The Code Starting here 👇
print("Welcome to tip calculator.")
bill = float(input("What was the total bill? $"))
percantage_tip = int(input("What percantage tip you would like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_with_bill = percantage_tip/100 * bill + bill
bill_per_person = tip_with_bill / people
final_amount = (round(bill_per_person, 2))
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay : ${final_amount}")
