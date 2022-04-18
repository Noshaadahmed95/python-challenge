import os
import csv
csvpath = os.path.join("/Users/nosha/anaconda3/Bootcamp_Work/Local Repo/python-challenge/PyPoll/Resources/election_data.csv")
out_file = os.path.join("/Users/nosha/anaconda3/Bootcamp_Work/Local Repo/python-challenge/PyPoll/Py_Poll.txt")

vote_total = 0
vote_candidates = {}
list_candidates = []
winning_count = 0
winning_candidates = ""


with open(csvpath) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    
    for row in reader: 
        print(".", end=""),
    
        vote_total = vote_total + 1

        name_candidates = row[2]

        if name_candidates not in list_candidates:

            list_candidates.append(name_candidates)

            vote_candidates[name_candidates] = 0

        vote_candidates[name_candidates] = vote_candidates[name_candidates] + 1

with open(out_file, "w") as txt_file:

    election_results = (
        f"n\nElection Results\n"
        f"--------------------------------------------------------\n"
        f"Total Votes: {vote_total}\n"
        f"--------------------------------------------------------\n")
    print(election_results)

    for candidate in vote_candidates:
        
        votes = vote_candidates.get(candidate)
        vote_percentage = float(votes) / float(vote_total) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
    
            
winning_candidate_summary = (
       f"--------------------------------------------------------\n"
       f"Winner: {winning_candidate}\n")

print(winning_candidate_summary)

file1=open("pypoll.txt","w")
file1.writelines(winning_candidate_summary)
file1.close()