# Write your solution here
meals_at_cafeteria = int(
    input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
groceries_expenditure = float(
    input("How much money do you spend on groceries in a week?"))
weekly_expenditure = meals_at_cafeteria * lunch_price + groceries_expenditure
daily_expenditure = weekly_expenditure/7
print("\nAverage food expenditure:")
print(f"Daily: {daily_expenditure} euros")
print(f"Weekly: {weekly_expenditure} euros")
