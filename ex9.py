initial_monthly_salary = float(input("How much do you earn per year? ")) / 12
semi_annual_raise = 0.07
annual_return = 0.04
downpayment_proportion = 0.25
total_cost = 1000000
months_limit = 36
current_savings = 0
downpayment = total_cost * downpayment_proportion

lower = 0
upper = 1
counter = 0
monthly_salary = initial_monthly_salary

for x in range(1, 37):  # runs 36 times
    current_savings += current_savings + current_savings * (annual_return / 12)  # adds monthly interest
    current_savings += monthly_salary * 1  # adds a proportion of wages
    if x % 6 == 0:
        monthly_salary += monthly_salary * (semi_annual_raise / 12)
if current_savings < (total_cost * downpayment_proportion):
    print("It is not possible to meet the downpayment in 36 months.")
else:
    current_savings = 0
    while (current_savings < downpayment-100) and (current_savings > downpayment+100):
        print("attempt")
        if counter > 0:
            if current_savings > (total_cost * downpayment_proportion):
                upper = (upper - lower) / 2
            else:
                lower = (upper - lower) / 2
        current_savings = 0
        monthly_salary = initial_monthly_salary
        for x in range(1, 37):  # runs 36 times
            current_savings += current_savings + current_savings * (annual_return / 12)  # adds monthly interest
            current_savings += monthly_salary * ((upper - lower) / 2)  # adds a proportion of wages
            if x % 6 == 0:
                monthly_salary += monthly_salary * (semi_annual_raise / 12)
        counter += 1
    print("The optimum saving rate to meet the downpayment in 36 months is {0}.".format((upper - lower) / 2))
    print("This calculation took {0} steps.".format(counter))
