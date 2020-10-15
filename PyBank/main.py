# Modules/Dependencies
import os
import csv

# set path for file
budget_path = os.path.join("Resources", "budget_data.csv") 

# Lists to store data/ Variables
total_months = 0
net_total_amount = 0
total_monthly_change =0
previous_profit_loss = 0
monthly_change = 0
average_monthly_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""


# Open and read the CSV

with open(budget_path, "r") as file:

# CSV Reader Specifies Delimiter 
  csvreader = csv.reader(file, delimiter=",")

# Read the header row first
  csvheader = next(csvreader)
  
  for row in csvreader:
      
    # calculating the total number of months in the dataset
      total_months +=1

    # calculating the net total amount of "Profit/Losses"    
      net_total_amount+= int(row[1])

    # Calculate Change From Previous Month to Current Month  

      if total_months  > 1:
        monthly_change = (int(row[1])- previous_profit_loss)

      # add up the total monthly change, used later to calculate average  
      total_monthly_change += monthly_change

      # set profit/loss value for previous month
      previous_profit_loss= int(row[1])
      
      # calculate greatest increase in profits
      if monthly_change > greatest_increase:
         greatest_increase = monthly_change
         greatest_increase_month=(row[0])

      # calculate greatest decrease in losses
      if monthly_change < greatest_decrease :
          greatest_decrease =monthly_change
          greatest_decrease_month = (row[0])
         
# calculate average change between months 
average_monthly_change = round(total_monthly_change/(total_months-1),2) 

     
 # Print the analysis to terminal    
print(f"Financial Analysis")   
print("---------------------------- ") 

print(f"Total Months: {total_months}")

print(f"Total: ${net_total_amount}")

print(f"Average Change ${average_monthly_change}")

print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")

print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


#set path for analysis
budget_analysis = os.path.join(".", 'PyBank',"Analysis","budget_analysis.txt") 

with open("budget_analysis", "w") as txtfile:


# Write Data to text file
    
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_monthly_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
