#income =input("Enter your monthly income:")
#expenses =input("Enter your total monthly expenses:")
#Monthly_Savings =int(income)-int(expenses)
#Savings = round(Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05))
#print("Your monthly savings are $"+ str(Monthly_Savings))
#print("Projected savings after one year, with interest, is: $" + str(Savings) + ".")
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")
monthly_savings = float(monthly_income) - float(monthly_expenses)


#annual interest rate of 5%
annual_interest_rate = 0.05

#projection over one year
annual_savings = monthly_savings * 12
annual_interest = annual_savings * annual_interest_rate

#final output
projected_savings = annual_savings + annual_interest

print("Your monthly savings are $: ",monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)
