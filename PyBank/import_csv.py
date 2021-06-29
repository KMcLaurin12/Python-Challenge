import csv
import os


Months = 0
Profits = []
change = 0
Dates = []
total_net_change = 0
filepath = os.path.join("Resources","budget_data.csv")
with open(filepath) as csv_file:

    csv_reader = csv.reader(csv_file)
    csvheader = next(csv_reader)
    jan_data = next(csv_reader)
    Months += 1
    total_net_change += int(jan_data[1])
    previous_net = int(jan_data[1])
    for row in csv_reader:
        

        Months += 1
        total_net_change += int(row[1])
        change = int(row[1])- previous_net
        previous_net = int(row[1])
        Profits.append(change)
avg_change = round((sum(Profits)/len(Profits)), 2)
print(Months, total_net_change, avg_change)