import csv
import os
with open("Resources/budget_data.csv") as csv_file:
  Months = 0
  Profits = []
  Dates = []
  csv_reader = csv.reader(csv_budget_data.csv)

  for row in open("budget_data.csv"):
    num_rows += 1
    print(num_rows)

    csvreader = csv.reader(csv_file)
    first_row = next(csvreader)

  for row in csvreader:
    total_months += 1
    total_net_change += int(row[1])

    print(net_change_list)

  max_value = max(numbers)
print('Maximum value:', max_value)

mean_value = mean(numbers)
print('Mean value:', mean_value)

range_value = range("Profit")
print(range_value)

range_vaue = range("Losses")
print(range_value)

budget_csv = os.path.join('budget_data.csv')

#Open the CSV
with open(budget_csv, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")

    #Skip the header row
    next(budget_reader)

    #Loop through the CSV file
    for row in budget_reader:

        #Add date
        months.append(row[0])

        #Add Profit/Loss
        profit_loss.append(float(row[1]))

#Calculate the total months included in the data set
total_months = (len(months))

#Calculate the net amount of Profit/Losses over the period of time
net_amount = sum(profit_loss)

#Calculate the average change per month
avg_change = net_amount / total_months

#Calculate the greatest increase in profits (date and amount)
max_profit = max(profit_loss)

#Using the index of the greatest increase to find the date
index_max = profit_loss.index(max_profit)
max_month = months[index_max]

#Calculate the greatest decrease in loss (date and amount)
min_profit = min(profit_loss)

#Using the index of the greatest decrease to find the date
index_min = profit_loss.index(min_profit)
min_month = months[index_min]

financial_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {max_month} {max_profit:.2f}
Greatest Decrease in Profits: {min_month} {min_profit:.2f}''')

#Print out analysis
print(financial_analysis)

#Create a .txt file containing the same analysis in the print out
analysis = open('financial_analysis.txt', 'w')

analysis.write(financial_analysis)

analysis.close()