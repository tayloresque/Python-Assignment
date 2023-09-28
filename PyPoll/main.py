import os
import csv

#create vote counter
total_votes = 0

#set list of candidates options and votes
candidate_options = []
candidate_votes = {}

#path to collect data
election_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'Resources',
    'election_data.csv')

#open and read file
with open (election_file_path, 'r') as election_csv:
    election_rows = csv.reader(election_csv, delimiter=",")

    #skip header row
    next(election_rows)

    #loop through rows
    for row in election_rows:

        #calculate total votes
        total_votes += 1

        #get the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match a name in the list, add it to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

        #and begin tracking that candidates vote counter
            candidate_votes[candidate_name] = 0

        #add a vote to that candidates count
        candidate_votes[candidate_name] += 1

    #calculate percentage of votes for each candidate  
    candidate_percentage = {key: round(val / total_votes * 100,3) for key, val in candidate_votes.items()} 
    winning_candidate = max(candidate_votes, key=candidate_votes.get)            

# Export as a text file
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'PyPoll_Results.txt')

with open(output_file_path, "w+") as f:
    f.write("Election Results\n")
    f.write("---------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("---------------------------\n")

    for k, v in candidate_votes.items():
        f.write(f'{k}: {candidate_percentage[k]}% ({v})\n')
    
    f.write("---------------------------\n")
    f.write(f"Winner: {winning_candidate}\n")
    f.write("---------------------------\n")