import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    store_list = [row for row in csvreader]

store_list.pop(0)
total_votes = len(store_list) #Q1
Charles_votes = 0
Diana_votes = 0
Ray_votes = 0
for row in store_list:
    if row[2] == "Charles Casper Stockham":
        Charles_votes += 1
    elif row[2] == "Diana DeGette":
        Diana_votes += 1
    elif row[2] == "Raymon Anthony Doane":
        Ray_votes += 1

winner_count = max([Charles_votes,Diana_votes,Ray_votes])
if winner_count == Charles_votes:
    winner = "Charles Casper Stockham"
elif winner_count == Diana_votes:
    winner = "Diana DeGette"
elif winner_count == Ray_votes:
    winner = "Raymon Anthony Doane"

print("Election Results")
print("-------------------------")
print("Total votes: " + str(total_votes))
print("-------------------------")
print(f"Charles Casper Stockham: {round((Charles_votes/total_votes)*100,3)}% ({Charles_votes})")
print(f"Diana DeGette: {round((Diana_votes/total_votes)*100,3)}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {round((Ray_votes/total_votes)*100,3)}% ({Ray_votes})")
print("-------------------------")
print("Winner: " + str(winner))

output_path = os.path.join("analysis", "analysis.csv")
with open(output_path, 'w') as csvfile:
    csvfile.write("Election Results" + '\n')
    csvfile.write("-------------------------" + '\n')
    csvfile.write("Total votes: " + str(total_votes) + '\n')
    csvfile.write("-------------------------" + '\n')
    csvfile.write(f"Charles Casper Stockham: {round((Charles_votes/total_votes)*100,3)}% ({Charles_votes})" + '\n')
    csvfile.write(f"Diana DeGette: {round((Diana_votes/total_votes)*100,3)}% ({Diana_votes})" + '\n')
    csvfile.write(f"Raymon Anthony Doane: {round((Ray_votes/total_votes)*100,3)}% ({Ray_votes})" + '\n')
    csvfile.write("-------------------------" + '\n')
    csvfile.write("Winner: " + str(winner) + '\n')

    
