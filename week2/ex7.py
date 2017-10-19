import math

annual_salary = float(input("How much do you earn per year? "))
portion_saved = float(input("What proportion of your income will you save? "))
total_cost = float(input("How much does your dream house cost? "))

portion_deposit = 0.2
current_savings = 0
monthly_interest = current_savings * (0.04 / 12)
monthly_salary = annual_salary / 12

months_required = math.ceil((portion_deposit * total_cost) / ((monthly_salary * portion_saved) + monthly_interest))
print("Number of months:", months_required)
