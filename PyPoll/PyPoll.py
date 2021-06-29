import os
import csv


total_votes = 0
candidates_votes = {}
candidate_list = []

with open('election_data.csv')

csvreader = csv.reader(csv_file,delimiter=',')
header = next(csvreader)

for row in csvreader
total_votes = total_votes + 1
candidate_name = row[2]


print.max_value(candidate)

with open(voter_csv, newline="") as csvfile:
    voterreader = csv.reader(csvfile, delimiter=",")

    #Skip header row
    next(voterreader)

    #Loop through the rows of data
    for row in voterreader:

        #Count total votes
        vote_total += 1

        #Count votes for each candidate
        if row[2] in vote_count:
            vote_count[row[2]] += 1

         #If the candidate does not exist in the dictionary add them and set value as 1
        else:
            vote_count[row[2]] = 1

#Create a variable to hold the winner vote count
winner_count = 0

#Loop through vote_count dictionary to calculate the vote percentage and to determine the winner
for candidate in vote_count:
    
    #Calculate and store candidate vote percentage
    vote_per[candidate] = (vote_count[candidate] / vote_total) * 100

    #Determine the winner
    if vote_count[candidate] > winner_count:
        winner_count = vote_count[candidate]
        winner = candidate

#Print out the results while writing them to a text file
results_path = os.path.join('election_results.txt')

with open(results_path, 'w', newline="") as txtfile:

    txtfile.write(f'''
Election Results
-------------------------
Total Votes: {vote_total}
-------------------------\n''')

    print(f'''\nElection Results
-------------------------
Total Votes: {vote_total}
-------------------------''')

    for candidate, votes in vote_count.items():
        txtfile.write(f'{candidate}: {vote_per[candidate]:.3f}% ({votes})\n')
        print(f'''{candidate}: {vote_per[candidate]:.3f}% ({votes})''')
    
    txtfile.write(f'''-------------------------
Winner: {winner}
-------------------------''')

    print(f'''-------------------------
Winner: {winner}
-------------------------''')