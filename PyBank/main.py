import os
import csv

# list variables
total_months = 0
total_profit_losses = 0 
previous_profit_loss = 0
profit_loss_change = []
max_increase = {"date": "", "amount": 0}
max_decrease = {"date": "", "amount": 0}
change_total = 0

#path to collect data 
budget_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'Resources',
    'budget_data.csv')

#open and read file
with open(budget_file_path, 'r') as budget_csv: 
    budget_rows = csv.reader(budget_csv, delimiter= ",")
    
    #skip header row
    next(budget_rows)

    # loop over each of the rows
    for row in budget_rows:
        total_months += 1
        
        # add the value from each row into the global value total_profit_losses
        date = row[0]
        profit_losses = int(row[1])
        total_profit_losses += profit_losses
        
        # look at the diff between current value and previous value
        if previous_profit_loss == 0:
            previous_profit_loss = profit_losses
        else: 
            decrease = profit_losses - previous_profit_loss
            profit_loss_change.append(decrease)

            # calculate change month over month
            if decrease >  max_increase["amount"]:
                max_increase["date"] = date
                max_increase["amount"] = decrease

            if decrease < max_decrease["amount"]:
                max_decrease["date"] = date
                max_decrease["amount"] = decrease
            change_total = decrease + change_total
            decrease = 0

            # memoize as previous value
            previous_profit_loss = profit_losses

pl = 0
for n in profit_loss_change:
    pl += 1

# Export as a text file
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PyBank_Results.txt')

with open(output_file_path, "w+") as f:
    f.write("Financial Analysis\n")
    f.write("--------------------------------\n")
    f.write("Total Months: " + str(total_months) + "\n")
    f.write("Total Profit Losses: $" + str(total_profit_losses) + "\n")
    f.write("Average Change: $" + str(round(change_total / pl, 2)) + "\n")
    f.write("Greatest Increase in Profits: " + max_increase["date"] + " ($" + str(max_increase["amount"]) + ")\n")
    f.write("Greatest Decrease in Profits: " + max_decrease["date"] + " ($" + str(max_decrease["amount"]) + ")\n")
    