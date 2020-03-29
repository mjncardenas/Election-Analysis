# The data we need to retrieve.
#1. The total number the votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular votes
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is,", now)
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is,", now)
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: perform analysis.
    print(election_data)
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.    
with open(file_to_save, "w") as txt_file:

 # Write some data to the file.
    txt_file.write("Hello World")
# Write three counties to the file.
    txt_file.write("Arapahoe")
    txt_file.write("Denver")
    txt_file.write("Jefferson")

# Close the file
txt_file.close()
 # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. Initializing a total vote counter
total_votes = 0
#candidate option
candidate_options = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
 
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
#Print the header row
    headers=next(file_reader)
    print(headers)
#Print each row in the CSV file.
    for row in file_reader:
       #2. Add to the total vote count.
       total_votes += 1

#3. Print the total vote count
print(total_votes)
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

        # Add it to the list of candidates.
        candidate_options.append(candidate_name)

# Print the candidate list.
print(candidate_options)