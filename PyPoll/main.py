#importing modules
import os
import csv

#setting variable's initial values 
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

#creating dictionarys to store candidate names and keys for vote count values

candidate = {"name": ["Khan", "Correy", "Li","O'Tooley"],
             "vote_count": [0, 0, 0, 0]}


#setting csv file path
csvpath = os.path.join("Resources", "election_data.csv")

#opening the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #this lets us skip the first row or the header of the csv file
    csvheader = next(csvreader)

    #using for loop to iterate through the rows in csv file
    for row in csvreader:

        #using the += to count each loop for a counter
        total_votes += 1

        #using if elif with names to tally vote counts through the for loop
        #candidates names will be the trigger for the variable counters += and give us the total number of votes for each name
        if row[2] == "Khan": 
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li": 
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1

#creating a list to hold the vote count values for each candidate.
vote_count = [khan, correy, li, otooley]

#replacing key "vote_count" values with total number of votes
candidate["vote_count"] = vote_count

#arithmatic to find percentage for easier print statement
khan_P = (khan/total_votes) * 100
correy_P = (correy/total_votes) * 100
li_P = (li/total_votes) * 100
otooley_P = (otooley/total_votes) * 100

#using the max() function to find the largest vote from dictionary
majority = max(candidate["vote_count"])

#using the list.index() to get the index number from dictionary and setting it to a variabel
index = vote_count.index(majority)

#getting the dictionary key "name" and converting it to a list to make use of the index
candidate_list = candidate["name"]

# Print the summary table
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {khan_P:.3f}% ({khan})")
print(f"Correy: {correy_P:.3f}% ({correy})")
print(f"Li: {li_P:.3f}% ({li})")
print(f"O'Tooley: {otooley_P:.3f}% ({otooley})")
print("----------------------------")
print(f"Winner: {candidate_list[index]}")
print("----------------------------")

#exporting write to file into Analysis folder
export = os.path.join('Analysis','Financial_Analysis.txt')
#creating a new file if it does not exist
with open(export,'w') as txt:
    txt.write("Election Results")
    txt.write("\n")
    txt.write("----------------------------")
    txt.write("\n")
    txt.write(f"Total Votes: {total_votes}")
    txt.write("\n")
    txt.write(f"Khan: {khan_P:.3f}% ({khan})")
    txt.write("\n")
    txt.write(f"Correy: {correy_P:.3f}% ({correy})")
    txt.write("\n")
    txt.write(f"Li: {li_P:.3f}% ({li})")
    txt.write("\n")
    txt.write(f"O'Tooley: {otooley_P:.3f}% ({otooley})")
    txt.write("\n")
    txt.write("----------------------------")
    txt.write("\n")
    txt.write(f"Winner: {candidate_list[index]}")
    txt.write("\n")
    txt.write("----------------------------")