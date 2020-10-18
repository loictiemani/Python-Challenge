# Modules/Dependencies
import os
import csv

# set path for file
election_path = os.path.join(".","PyPoll" ,"Resources","election_data.csv")

# Lists to store data/ Variables
total_votes = 0
Candidates = {}
win_percentage={}
All_percentage=[]

# Open and read the CSV
with open(election_path, "r") as file:

# CSV Reader Specifies delimiter 
    csv_reader = csv.reader(file,delimiter=",")
   
   # Read the header row first
    csv_header=next(csv_reader)
    
    for row in csv_reader:
       # Calculate Total Number Of Votes Cast 
        total_votes+=1

         # Calculate Total Number Of Votes Each Candidate Won
        if row[2] not in Candidates.keys():
        
            Candidates[row[2]]=1
        else:
            Candidates[row[2]]+=1
     # Calculate win_percentage of vote Each Candidate Won by creating new dictionary w     
    win_percentage = dict(Candidates)

#set path for analysis
Poll_analysis = os.path.join(".", "PyPoll","Analysis","Poll_analysis.txt") 

with open(Poll_analysis, "w") as txtfile:

     # Write Data to text file
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")

     # Print the analysis to terminal 
    print(f"Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    txtfile.write("--------------------------\n")

     # Calculate win_percentage of vote each Candidate Won
    for k,v in  win_percentage.items(): 
        win_percentage[k] =  round(v *100/ total_votes,2)
       # Print the candidate's win_percentage and total number of votes to terminal  
        print(f"{k}: {win_percentage[k]}% ({v})")

        #Create a list of percentages
        All_percentage.append(win_percentage[k])
        txtfile.write(f"{k}: {win_percentage[k]}% ({v})\n")
    print("--------------------------")
    txtfile.write("--------------------------\n")
    # Calculate Winner of the Election based on popular vote
    maximum_value = max(All_percentage)
    for k,v in  win_percentage.items():
        if v==maximum_value :
            print(f"Winner: {k}")
            txtfile.write(f"Winner: {k}\n")
    print("--------------------------")
    txtfile.write("--------------------------")
    