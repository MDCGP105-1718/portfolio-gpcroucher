import math

annual_salary = float(input("How much do you earn per year? "))
semi_annual_raise = float(input("By what proportion does your salary increase every six months? "))
portion_saved = float(input("What proportion of your income will you save? "))
total_cost = float(input("How much does your dream house cost? "))

portion_deposit = 0.2
current_savings = 0
investment_return = 0.04
monthly_interest = current_savings * (0.04 / 12)
monthly_salary = annual_salary / 12
'''
months_required = math.ceil((portion_deposit * total_cost) / ((monthly_salary * portion_saved) + monthly_interest))
print("Number of months:", months_required)
'''
months_required = 0
while current_savings < portion_deposit * total_cost:  # while savings is less than deposit
    for x in "abcdef": # runs six times
        current_savings += current_savings * (investment_return / 12)  # adds monthly interest
        current_savings += monthly_salary * portion_saved  # adds earnings
        months_required += 1  # increments months elapsed so far
    monthly_salary += monthly_salary * (semi_annual_raise / 12)  # adds raise every six months

print ("Number of months:", months_required)
