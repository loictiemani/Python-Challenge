# Modules/Dependencies
import os
import csv

# set path for file
election_path = os.path.join(".","PyPoll" ,"Resources","election_data.csv")



# Lists to store data/ Variables
total_votes = 0
total_votesc = 0
Candidates_with_votes = []

# Open and read the CSV
with open(election_path, "r") as file:

# CSV Reader Specifies Delimiter 
    csv_reader = csv.reader(file,delimiter=",")
   
   # Read the header row first
    csv_header=next(csv_reader)
    
    for row in csv_reader:
       
       total_votes+=1
       
       if row[2] not in Candidates_with_votes:
        
           Candidates_with_votes.append(row[2])
        
       if row[2] == Candidates_with_votes[0]:

            total_votesc+=1   
       percentage = total_votesc/total_votes


print(f"Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")  
print("--------------------------")   
print(f"{Candidates_with_votes}") 
print(f"Total Votes: {total_votesc}") 
print(f"{percentage}")