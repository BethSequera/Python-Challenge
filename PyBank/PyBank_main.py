import csv
with open(r'C:\Users\Marly\OneDrive - RPAutomation Consulting\Desktop\github\Python_Challenge\PyBank\Resources\budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    total_months = 0
    net_profit_loss = 0
    prev_month_profit_loss = 0
    profit_loss_change_list = []
    month_list = []

    for row in reader:

        total_months += 1

        net_profit_loss += int(row[1])

        profit_loss_change = int(row[1]) - prev_month_profit_loss

        if total_months > 1:
            profit_loss_change_list.append(profit_loss_change)

        prev_month_profit_loss = int(row[1])

        month_list.append(row[0])

    average_profit_loss_change = sum(profit_loss_change_list) / len(profit_loss_change_list)

    max_profit_loss_change = max(profit_loss_change_list)
    max_profit_loss_change_index = profit_loss_change_list.index(max_profit_loss_change)
    max_profit_loss_change_month = month_list[max_profit_loss_change_index + 1]
    max_profit_loss_change_formatted = f"${max_profit_loss_change:,}"
    min_profit_loss_change = min(profit_loss_change_list)
    min_profit_loss_change_index = profit_loss_change_list.index(min_profit_loss_change)
    min_profit_loss_change_month = month_list[min_profit_loss_change_index + 1]
    min_profit_loss_change_formatted = f"${min_profit_loss_change:,}"

print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss:,}")
print(f"Average Change: ${average_profit_loss_change:.2f}")
print(f"Greatest Increase in Profits: {max_profit_loss_change_month} ({max_profit_loss_change_formatted})")
print(f"Greatest Decrease in Profits: {min_profit_loss_change_month} ({min_profit_loss_change_formatted})")

with open('financial_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_profit_loss:,}\n")
    file.write(f"Average Change: ${average_profit_loss_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {max_profit_loss_change_month} ({max_profit_loss_change_formatted})\n")
    file.write(f"Greatest Decrease in Profits: {min_profit_loss_change_month} ({min_profit_loss_change_formatted})\n")

print("The financial analysis has been exported to 'financial_analysis.txt'")
total_votes = 0
