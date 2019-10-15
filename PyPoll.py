#Dependencies
import csv
import os

def recordVotes(ballot, optionList, optionTally):
    name = ballot
    if name not in optionList:
        optionList.append(name)
        optionTally[name] = 0
    optionTally[name] += 1

def calculateVotes(name, count, percentage, tally, total_votes):
    #For each item in the dictionary, print out the name, vote percentage & vote Total
    for item in tally:
        votes = tally[item]
        calculatedPercentage = (votes/total_votes) * 100
        results = (f"{item}: {calculatedPercentage:.1f}% ({votes:,})\n")

        #Print Results
        print(results)
        txt_file.write(results)

        #Determine item with largest share of the votes
        if (votes > count) and (calculatedPercentage > percentage):
            count = votes
            percentage = calculatedPercentage
            name = item
    return name, count, percentage  # Returns a tuple of the largest objects name, vote count, and percentage of total votes


#Assign a variable for the file to load
file_to_load = os.path.join("Resources","election_results.csv")
#Create filename 
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Initializations
total_votes = int()
total_votes = 0

###Candidate Options
candidate_options = []
###Candidate Tally
candidate_votes = {}
###Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

###County Options
countyList = []
###County Tally
countyTally = {}
###Largest County Vote total 
largestCounty = ""
largestCountyCount = 0
largestCountyCountPercentage = 0

#Open the results & Read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read the header row
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        #Call recordVotes function to add item to list & record add to total
        recordVotes(row[2], candidate_options, candidate_votes)   #Candidate Total
        recordVotes(row[1], countyList, countyTally)             #County Total

#using the open funtion with the "w" mode we will write data to the file
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    txt_file.write(election_results)

    #County Vote Statistics
    countyVoteHeader = "County Votes\n"
    print(countyVoteHeader)
    txt_file.write(countyVoteHeader)
    
    #calculate & print county statistics
    largestCounty = calculateVotes(largestCounty, largestCountyCount, largestCountyCountPercentage, countyTally, total_votes)
    
    #print county with largest vote share
    largestCountySummary = (
        f"\n--------------------------\n"
        f"Largest County Turnout: {largestCounty[0]}\n"
        f"--------------------------\n")
    print(largestCountySummary)
    txt_file.write(largestCountySummary)

    #calculate candidate vote totals
    winner = calculateVotes(winning_candidate, winning_count, winning_percentage, candidate_votes, total_votes)
    
    #print winner & summary
    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winner[0]}\n"
        f"Winning Vote Count: {winner[1]:,}\n"
        f"Winning Percentage: {winner[2]:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)