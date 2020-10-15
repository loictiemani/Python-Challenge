# Modules/Dependencies

import os
import csv

#set path for file
csvpath = os.path.join("Resources", "budget_data.csv") 

# Lists to store data

total_months = 0
Total_months =[]
net_total_amount = 0
Monthly_change = []
average_changes = 0
greatest_increase = 0
greatest_increaser_month = []
greatest_decrease = 0
greatest_decrease_month = []
previous_value = 0




# Open and read the CSV

with open(csvpath, "r") as file:

# CSV Reader Specifies Delimiter 
  csvreader = csv.reader(file, delimiter=",")

  csvheader = next(csvreader)

  for row in csvreader:
      
    #calculating the total number of months in the dataset
      total_months +=1

    #calculating the net total amount of "Profit/Losses"    
      net_total_amount+= int(row[1])

    # Calculate Change From Current Month To Previous Month  

      previous_value = int(row[1])                               


      if total_months > 0:
            Monthly_change.append (int(row[1])- previous_value)
            previous_value = int(row[1])
      #change_1_month= int(row[1])-(previous_value)
    
average_changes = round(sum(Monthly_change)/len(Monthly_change),2)
    
     
    
print(f"total number of months {total_months}")
print(net_total_amount)
#print(change_1_month)

#print (Monthly_change)
print (average_changes)