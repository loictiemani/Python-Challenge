# Modules/Dependencies
import os
import csv

# set path for file
election_path = os.path.join(".","PyPoll" ,"Resources","election_data.csv")

# Lists to store data/ Variables
total_votes = 0
Candidates = {}
percentage={}
AllValues=[]

# Open and read the CSV
with open(election_path, "r") as file:

# CSV Reader Specifies Delimiter 
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
     # Calculate percentage of vote Each Candidate Won by creating new dictionary w     
    percentage = dict(Candidates)

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

     # Calculate percentage of vote Each Candidate Won
    for k,v in  percentage.items(): 
        percentage[k] =  round(v *100/ total_votes,2)
       # Print the candidate's percentage and total number of votes to terminal  
        print(f"{k}: {percentage[k]}% ({v})")
        AllValues.append(percentage[k])
        txtfile.write(f"{k}: {percentage[k]}% ({v})\n")
    print("--------------------------")
    txtfile.write("--------------------------\n")
    # Calculate Winner Of The Election Based On Popular Vote
    maximum_value = max(AllValues)
    for k,v in  percentage.items():
        if v==maximum_value :
            print(f"Winner: {k}")
            txtfile.write(f"Winner: {k}\n")
    print("--------------------------")
    txtfile.write("--------------------------")