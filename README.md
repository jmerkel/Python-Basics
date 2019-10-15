# Election_Analysis
Python Basics

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election

1. Calculate the total number of votes
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes
  - Diana DeGette received 73.8% of the vote and 272,892 total votes
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes
- The winner of the election was:
  - Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Challenge Overview
Refactor the code to provide county vote statistics

## Challenge Summary
- County Votes
  - Jefferson county provided 10.5% of the vote and 38,855 total votes
  - Denver county provided 82.8% of the vote and 306,055 total votes
  - Arapahoe county provided 6.7% of the vote and 24,801 total votes

The county with the largest turnout was Denver

### Challenge Code structure
Program logic now uses two functions:
- *recordVotes* to tally the vote of each ballot
- *calculateVotes* to record each data item's statistics as well as the largest object.

Logic to record county information has been added
