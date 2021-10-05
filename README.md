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

## Election-Audit Results:
* _Voter Turnout_: In total there were 369,711 votes cast.  As shown below, Denver county had the largest turnout (82.8%).

     ![CountyVotes](https://user-images.githubusercontent.com/90986041/135736602-081c9211-3954-467a-beaf-124104c9a9bc.png)

* _Candidate Results_: Diana DeGette easily won the election, receiving 73.8% (272,892) of the total votes cast.  As shown below, Charles Casper Stockholm was a distant second with 23.0% of the votes, followed by Raymon Anthony Doane with 3.1%.  
 
     ![CandidateVotes](https://user-images.githubusercontent.com/90986041/135736572-b93c699f-6947-4382-abec-2686ac56fa91.png)

## Election-Audit Summary
Candidates and their supporters anxiously await the results after each election.  Historically, election results have been manually tabulated and analyzed using Excel.  Manually processing large amounts of information is not only time-consuming, it is prone to error.  The introduction of this Python script is a game-changer! It accurately reads the data files, tabulates the vote counts, and analyzes the results automatically within seconds.  Additionally, it's use can be expanded for other congressional precincts, senatorial precincts, and local races. 

In its current state, the script processes data for one precinct at a time using a source file called "election_results.csv" and an output file called "election_results.txt".  

With minor modifications it can be utilized for other elections: 

* Updating the source data file (e.g., "election_results.csv") on row 9 of the script:
 
   file_to_load = os.path.join("Resources", "election_results.csv")
     
* Updating the output file (e.g., "election_results.txt") for the results on row 11 of the script:

     file_to_save = os.path.join("analysis", "election_results.txt")

Future enhancements to this script may include: 

1. Improving rounding precision:  The candidate vote percentages above do not total 100% due to rounding to one decimal place (.1f). Increasing the precision to two decimal places (.2f) fixes this issue.

_find code box formatting and include image of 2 decimal results._
    candidate_results = (
                f"{candidate_name}: {vote_percentage:.2f}% ({votes:,})\n")
                
1. Determining how many votes each candidate received within each county and the percentage of the county's total.

   _insert table with mocked up results
   
1. Adding a congressional district dictionary that includes the district and county.  If the whole state's election results are included in a single source file, the result summaries above could be tabulated by congressional district.

_insert table with mocked up results_

___
## Resources
_Data Source_: https://github.com/SJLewer/Election_Analysis/tree/main/Resources

_Data Analysis_: https://github.com/SJLewer/Election_Analysis/tree/main/analysis

_Python 3.7.6 Script_: https://github.com/SJLewer/Election_Analysis/blob/main/PyPoll_Challenge.py

_Analyst_: S. Lewer
