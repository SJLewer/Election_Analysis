# Election_Analysis

## Project Overview
A Colorado Board of Elections employee requested the followiong tasks be completed for the election audit of a recent local congressional election.

 #### Voter Turnout:
 1. Calculate the total number of votes cast
 1. Determine county with largest voter turnout

 #### Candidate Results:
 1. List of candidates who received votes
 1. Calculate the total number of votes each candidate received
 1. Calculate the percentage of votes each candidate won
 1. Determine the winner of the election based on popular vote

## Election-Audit Results
* _Voter Turnout_ : In total there were 369,711 votes cast in this congressional election.  As shown below, Denver county had the largest turnout (82.8%).

     ![CountyVotes](https://user-images.githubusercontent.com/90986041/135736602-081c9211-3954-467a-beaf-124104c9a9bc.png)

* _Candidate Results_: Diana DeGette easily won the election, receiving 73.8% (272,892) of the total votes cast.  As shown below, Charles Casper Stockholm was a distant second with 23.0% of the votes, followed by Raymon Anthony Doane with 3.1%.  
 
     ![CandidateVotes](https://user-images.githubusercontent.com/90986041/135736572-b93c699f-6947-4382-abec-2686ac56fa91.png)

## Election-Audit Summary
Candidates and their supporters anxiously await the results after each election.  Historically, election results have been manually tabulated and analyzed using Excel.  Manually processing large amounts of information is not only time-consuming, it is prone to error.  The introduction of this Python script is a game-changer! It accurately reads the data files, tabulates the vote counts, and analyzes the election results automatically within seconds.  

With minor modifications, this script can be used for other congressional precincts, senatorial precincts, and local races. 

1) Ask the user to enter name of precinct being audited and include this name on the output results.
```
# Ask user to enter name of precinct being audited
precinct = input ("Please enter name of precinct being audited: ")

# Print the final vote count (to terminal)
     election_results = (
         f"Election Results for {precinct}\n"
```

2) Allow the user to enter the unique .csv data filename and the unique .txt output filename for each precinct being audited. This facilitates preservation of each precinct's data and results.  It also eliminates the need for a programmer to change the underlying script each time a different district's votes are audited.
```
# Ask user to enter names of data input file and output file
fToLfile = input("Please enter .csv data filename (ex. p1_election_results.csv): ")
fToSfile = input("Please enter .txt output filename (ex. p1_election_results.txt): ")

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", fToLfile)

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", fToSfile)  
```     

3. Improve rounding precision:  The candidate vote percentages presented in the Election-Audit Results above do not total 100% due to rounding to one decimal place (.1f). Increasing the precision to two decimal places (.2f) fixes this issue.
```
candidate_results = (f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")
```             

   ![Candidate2fVotes](https://user-images.githubusercontent.com/90986041/136293135-3e198e0d-c20e-4dda-9ec5-634922bf097b.png)
___
## Resources
_Data Source_: https://github.com/SJLewer/Election_Analysis/tree/main/Resources

_Data Analysis_: https://github.com/SJLewer/Election_Analysis/tree/main/analysis

_Python 3.7.6 Script_: https://github.com/SJLewer/Election_Analysis/blob/main/PyPoll_Challenge.py

_Analyst_: S. Lewer
