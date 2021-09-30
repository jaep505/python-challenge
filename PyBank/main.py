#importing modules to use
import os
import csv

#creating empty list to hold the value
total_months = []
total_amount = []
monthly_change = []

#setting csv file path
csvpath = os.path.join("Resources", "budget_data.csv")

#opening the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #this lets us skip the first row or the header of the csv file
    csvheader = next(csvreader)

    #using for loop to iterate through the rows in csv file
    for row in csvreader:
        #using the .append() to append all the cell values in column 0 into a list
        total_months.append(row[0])

        #using the .append() to append all the cell values in column 1 as integer into a list
        total_amount.append(int(row[1]))

    #going through the total_amount list to find the changes, using the len()-1 to get correct index values in the list due to list index starting at 0
    for a in range(len(total_amount)-1):
        #obtain the monthly change by subtracting the next row from current row and append to a new list monthly_change
        monthly_change.append(total_amount[a+1] - total_amount[a])

#using the max() and min() to the monthly_change list to obtain maximum and minimum profit
max_profit = max(monthly_change)
min_profit = min(monthly_change)

#using the index value from the max_profit, we can find the correlating index value for the max_profit_month. add the 1 to index value for the list index starting at 0
max_profit_month = monthly_change.index(max(monthly_change)) + 1

#using the index value from the min_profit, we can find the correlating index value for the min_profit_month. add the 1 to index value for the list index starting at 0
min_profit_month = monthly_change.index(min(monthly_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: {sum(monthly_change)/len(monthly_change)}")
print(f"Greatest Increase in Profits: {total_months[max_profit_month]} (${(str(max_profit))})")
print(f"Greatest Decrease in Profits: {total_months[min_profit_month]} (${(str(min_profit))})")

#exporting write to file into Analysis folder
export = os.path.join('Analysis','Financial_Analysis.txt')
#creating a new file if it does not exist
with open(export,'w') as txt:
    txt.write("Financial Analysis")
    txt.write("\n")
    txt.write("----------------------------")
    txt.write("\n")
    txt.write(f"Total Months: {len(total_months)}")
    txt.write("\n")
    txt.write(f"Total: ${sum(total_amount)}")
    txt.write("\n")
    txt.write(f"Average Change: {sum(monthly_change)/len(monthly_change)}")
    txt.write("\n")
    txt.write(f"Greatest Increase in Profits: {total_months[max_profit_month]} (${(str(max_profit))})")
    txt.write("\n")
    txt.write(f"Greatest Decrease in Profits: {total_months[min_profit_month]} (${(str(min_profit))})")

