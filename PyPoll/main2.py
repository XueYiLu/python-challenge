# CSV file and store the data
with open("/Users/xueyilu/Desktop/Github/python-challenge/PyPoll/Resources/election_data.csv", "r") as file:
    lines = file.readlines()
    header = lines[0].strip().split(",")
    data = [dict(zip(header, line.strip().split(","))) for line in lines[1:]]

# Calculate the total number of votes cast
total_votes = len(data)

# Get a list of unique candidates
candidates = set(entry["Candidate"] for entry in data)

# Create a dictionary to store the total votes for each candidate
candidate_votes = {candidate: 0 for candidate in candidates}

# Calculate the total votes for each candidate
for entry in data:
    candidate_votes[entry["Candidate"]] += 1

# Calculate the percentage of votes each candidate won
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate in candidates:
    print(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = "/Users/xueyilu/Desktop/Github/python-challenge/PyPoll/Analysis/election_results.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")

    for candidate in candidates:
        file.write(f"{candidate}: {percentage_votes[candidate]:.3f}% ({candidate_votes[candidate]})\n")

    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"Results have been saved to {output_file}")
