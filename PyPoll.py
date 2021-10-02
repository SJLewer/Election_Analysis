#The data we need to retrive
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of vote each candidate won
#5. The winner of the election based on popular vote

#Add dependencies
import csv
import os

# Assign variable for the file to load and the path
file_to_load = os.path.join("Resources","election_results.csv")

#Assign a variable to save the file to path
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize a total vote counter, candidate list, candidate vote dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next (file_reader)
    
    #Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes +=1
        #Print the candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
            #candidate_votes[candidate_name]+=1
        candidate_votes[candidate_name]+=1
    
    #Calculate and print vote percentage for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        print (f"{candidate_name} received {votes} votes and {vote_percentage:.1f}% of the total votes.\n")
    
        #Determine the winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percentage
            
    winning_candidate_summary = (
        f"-------------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------------------\n")
    print (winning_candidate_summary)