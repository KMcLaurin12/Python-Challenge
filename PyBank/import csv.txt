import csv
import os
csv.path = "Resources/budget_data.csv"

budget_df = pd.read_csv(csv.path)
budget_df()