import os
import csv

PyPollcsv = os.path.join("Resources","election_data.csv")


with open(PyPollcsv) as csv_file:
	
	csvreader = csv.reader(csv_file, delimiter=",")
	
	header = next(csvreader)


	candidates_votes = {}
	candidates_votes_percentage = {}
	total_votes = 0
	
	
	for row in csvreader:
		
		if row[2] not in candidates_votes:
			candidates_votes[row[2]] = 1
		else:
			candidates_votes[row[2]] += 1
		
		total_votes += 1


	candidates_list = list(candidates_votes.keys())
        

	winner = max(candidates_votes.values())
        

	list_candidates_votes = list(candidates_votes.items())
     
    
	for candidates, votes in list_candidates_votes:
		
        
		votes_percentage = round(((votes/total_votes)*100),3)
		
		candidates_votes_percentage[candidates] = votes_percentage
		
        
		if votes == winner:
			winner_candidate = candidates



print(f"Election Results ")
print(f"-------------------------------")
print(f"Total Votes: {total_votes}")
print(f"{candidates_list[0]}: {candidates_votes_percentage[candidates_list[0]]}% ({candidates_votes[candidates_list[0]]})")
print(f"{candidates_list[1]}: {candidates_votes_percentage[candidates_list[1]]}% ({candidates_votes[candidates_list[1]]})")
print(f"{candidates_list[2]}: {candidates_votes_percentage[candidates_list[2]]}% ({candidates_votes[candidates_list[2]]})")
print(f"-------------------------------")
print(f"Winner : {winner_candidate}")
print(f"-------------------------------")




output_file = os.path.join("analysis","election_analysis_data.txt")
with open(output_file,"w",) as wf:

    wf.write(f"Election Results \n")
    wf.write(f"------------------------------\n")
    wf.write(f"Total Votes: {total_votes}\n")
    wf.write(f"{candidates_list[0]}: {candidates_votes_percentage[candidates_list[0]]}% ({candidates_votes[candidates_list[0]]})\n")
    wf.write(f"{candidates_list[1]}: {candidates_votes_percentage[candidates_list[1]]}% ({candidates_votes[candidates_list[1]]})\n")
    wf.write(f"{candidates_list[2]}: {candidates_votes_percentage[candidates_list[2]]}% ({candidates_votes[candidates_list[2]]})\n")
    wf.write(f"------------------------------\n")
    wf.write(f"Winner : {winner_candidate}\n")
    wf.write(f"------------------------------\n")
