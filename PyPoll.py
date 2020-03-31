# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1.  Initialize a total votes counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1
            # 1. Iterate through the candidate list.
with open(file_to_save, "w") as text_file:
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        # Save the final vote count to the text file.
        txt_file.write(election_results)   
        for candidate in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            print(candidate_results)
            txt_file.write(candidate_results)
        
            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage
                # Print the winning candidates' results to the terminal.
                winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
                print(winning_candidate_summary) 
                candidate_votes[candidate_name] += 1
                #Save the results to text file
                txt_file.write(winning_candidate_results)