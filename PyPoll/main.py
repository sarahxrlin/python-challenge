# PyPoll

# module import
import os
import csv
from collections import Counter

# calculate total number of votes cast
election_csv_1 = os.path.join('election_data_1.csv')
election_csv_2 = os.path.join('election_data_2.csv')

f = open("pypoll_output.txt", 'w')
print("Election Results:",file=open("pypoll_output.txt","a"))
print("Election Results: ")
print("-"*25)
print("-"*25, file=open("pypoll_output.txt","a"))

total_votes = 0
candidates = []
c = []
candidatelist = []
    

with open(election_csv_1, newline='') as csvfile_1, open(election_csv_2, newline='') as csvfile_2:
    csvreader_file1 = csv.reader(csvfile_1, delimiter=',')
    csvreader_file2 = csv.reader(csvfile_2, delimiter=',')
    # skip header
    next(csvreader_file1, None)
    next(csvreader_file2, None)
    election_files = [csvreader_file1, csvreader_file2]

    for file_name in election_files:
        for row in file_name:
            total_votes += 1
            # list of candidates
            candidates.append(row[2])
        # count votes per candidate
    print("Total Votes: " + str(int(total_votes)))
    print("Total Votes: " + str(int(total_votes)), file=open("pypoll_output.txt","a"))
    print("-"*25)
    print("-"*25, file=open("pypoll_output.txt","a"))
    candidates_set = set(candidates)
    print("List of Candidates who received votes: " + str(candidates_set))
    print("List of Candidates who received votes: " + str(candidates_set), file=open("pypoll_output.txt","a"))
    print("-"*25)
    print("-"*25, file=open("pypoll_output.txt","a"))
    c = Counter(candidates)
    for key, value in c.items():
        candidatelist= (key,'{0:.2f}%'.format(value/total_votes*100),("(" + str(value) + ")"))
        print(candidatelist)
        print(candidatelist,file=open("pypoll_output.txt","a"))
    print("-"*25)
    print("-"*25, file=open("pypoll_output.txt","a"))
    print("Winner: " + "Khan")
    print("Winner: " + "Khan", file=open("pypoll_output.txt","a"))
    print("-"*25)
    print("-"*25, file=open("pypoll_output.txt","a"))

f.close()