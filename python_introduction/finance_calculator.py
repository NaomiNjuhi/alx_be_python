monthly_income = int(input ("Enter your monthly income:"))
monthly_expenses = int (input ("Enter your total monthly expenses:"))
#Monthly savings
monthly_savings = monthly_income - monthly_expenses
#Annual savings
#(Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print ("Your monthly savings are", monthly_savings)
print ("Projected savings after one year, with interest, is:", projected_savings)2