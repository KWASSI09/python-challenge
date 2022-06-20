import os
import csv

PyBankcsv = os.path.join("Resources","budget_data.csv")

total_months = 0
total_profit = 0
monthly_change = []
months = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0
Initial_profit = []


with open(PyBankcsv) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    
    header = next(csvreader)
    row = next(csvreader)

    initial_profit = int(row[1])
    total_months = total_months + 1
    total_profit = total_profit + int(row[1])
    
    
    for row in csvreader:
        
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        profit_change = int(row[1]) - initial_profit
        monthly_change.append(profit_change)
        initial_profit = int(row[1])

        average_change = round ((sum(monthly_change)/ len(monthly_change)), 2)

        months.append(row[0])
        
        
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
        greatest_increase_profits = max(monthly_change)
        greatest_decrease_profits = min(monthly_change)

print(f"Financial Analysis")
print(f"--------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month}, (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${greatest_decrease_profits})")



final_file = os.path.join("..","PyBank","analysis","budget_data_analysis.txt")
with open(final_file, "w",) as wf:

    wf.write(f"Financial Analysis\n")
    wf.write(f"-------------------------------------\n")
    wf.write(f"Total Months: {total_months}\n")
    wf.write(f"Total: ${total_profit}\n")
    wf.write(f"Average Change: ${average_change}\n")
    wf.write(f"Greatest Increase in Profits: {greatest_increase_month}, (${greatest_increase_profits})\n")
    wf.write(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${greatest_decrease_profits})\n")